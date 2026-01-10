# Filename: integration_bridge/bridge.py
# UrbanPulse Integration Bridge
# Role: Deterministic transport + observability layer (NO safety logic)

import json
import time
import os

# ===================== CONFIG =====================
DEMO_MODE   = True          # True = FPGA simulated, False = real UART
SERIAL_PORT = "COM3"        # Change only if using real hardware
BAUD_RATE   = 115200
VERSION     = "1.0-prod-demo"

# ===================== STATUS CODES =====================
STATUS_OK     = 0x00  # Nominal
STATUS_VETO   = 0x01  # Grid clamp
STATUS_THERM  = 0x02  # Thermal lockout

# ===================== ANSI COLORS =====================
CYAN   = "\033[96m"
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
RESET  = "\033[0m"

# ===================== LOGGER =====================
def log(tag, message, color=RESET):
    ts = time.strftime("%H:%M:%S")
    print(f"{color}[{ts}] [{tag}] {message}{RESET}")

# ===================== FPGA RESPONSE MODEL =====================
def simulate_fpga_response(request_kw):
    """
    FPGA response model (BLACK BOX).
    NOTE:
    - Logic authority exists ONLY in Verilog.
    - This function represents a hardware response interface.
    """
    GRID_LIMIT_HARD = 200

    if request_kw > GRID_LIMIT_HARD:
        return GRID_LIMIT_HARD, STATUS_VETO
    return request_kw, STATUS_OK

# ===================== MAIN BRIDGE =====================
def run_bridge():
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{CYAN}==================================================")
    print(f"🌉 URBANPULSE INTEGRATION BRIDGE  |  v{VERSION}")
    print(f"🔗 MODE: {'SIMULATED FPGA' if DEMO_MODE else 'PHYSICAL UART'}")
    print(f"=================================================={RESET}\n")

    # -------- READ AI PLAN --------
    try:
        log("BRIDGE", "Loading plan.json from LLM Planner...", YELLOW)
        with open("../llm_planner/plan.json", "r") as f:
            data = json.load(f)
        log("BRIDGE", "Plan loaded successfully.", GREEN)
    except FileNotFoundError:
        log("ERROR", "plan.json not found. Run planner.py first.", RED)
        return

    # -------- UART SETUP (OPTIONAL) --------
    ser = None
    if not DEMO_MODE:
        try:
            import serial
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
            log("UART", f"Connected to FPGA on {SERIAL_PORT}", GREEN)
        except ImportError:
            log("ERROR", "pyserial not installed. Run: pip install pyserial", RED)
            return
        except Exception as e:
            log("ERROR", f"UART connection failed: {e}", RED)
            return

    print("\n" + "-" * 56)

    # -------- EXECUTION LOOP --------
    for step in data["plan"]:
        hour = step["hour"]
        requested_kw = step["total_kw"]

        log("INPUT", f"Hour {hour}: AI requesting {requested_kw} kW", CYAN)
        log("UART", "Sending raw request to FPGA...", CYAN)
        time.sleep(1)

        # ---- HANDSHAKE ----
        if DEMO_MODE:
            safe_kw, status = simulate_fpga_response(requested_kw)
        else:
            ser.write(requested_kw.to_bytes(2, byteorder="big"))
            response = ser.read(3)
            if len(response) != 3:
                log("UART", "FPGA response timeout!", RED)
                continue
            safe_kw = int.from_bytes(response[0:2], "big")
            status  = response[2]

        # ---- STATUS DECODE ----
        if status == STATUS_VETO:
            log("SENTINEL", "⚠️ HARDWARE VETO ASSERTED", RED)
            log("ACTION", f"CLAMPED {requested_kw} kW → {safe_kw} kW", YELLOW)
        elif status == STATUS_THERM:
            log("SENTINEL", "🔥 THERMAL LOCKOUT", RED)
            log("ACTION", "POWER CUT TO 0 kW", RED)
        else:
            log("SENTINEL", "✅ STATUS NOMINAL", GREEN)
            log("ACTION", f"APPROVED {safe_kw} kW", GREEN)

        print("-" * 56)
        time.sleep(1.5)

    # -------- CLEANUP --------
    if ser is not None:
        ser.close()

    print(f"\n{GREEN}✅ BRIDGE EXECUTION COMPLETE — SYSTEM STABLE.{RESET}")

if __name__ == "__main__":
    run_bridge()