import json

# HARDWARE CONSTANTS (Mirroring Verilog Parameters)
GRID_LIMIT_HARD = 200

# STATUS CODES (Mirroring Verilog Output)
STATUS_OK = 0x0      # 00
STATUS_VETO = 0x1    # 01 (Grid Clamp)
STATUS_THERMAL = 0x2 # 10 (Temp Trip)

# DECODING MAP (For Cleaner Logs)
STATUS_MAP = {
    STATUS_OK: " PASS",
    STATUS_VETO: " VETO (GRID CLAMP)",
    STATUS_THERMAL: " VETO (THERMAL TRIP)"
}

def mock_fpga_hardware_gate(requested_kw):
    """
    Simulates GreenFlow FPGA Verilog Logic.
    Input: Unsafe AI Request
    Output: Physically Enforced Limit + Hex Status Code
    
    # NOTE: This function mirrors greenflow_gate.v logic line-for-line.
    """
    # Deterministic Hardware Logic
    if requested_kw > GRID_LIMIT_HARD:
        return GRID_LIMIT_HARD, STATUS_VETO
    return requested_kw, STATUS_OK

def run_safety_bridge():
    print("\n GREENFLOW FPGA SAFETY BRIDGE INITIALIZED")
    print("="*60)
    
    try:
        with open('plan.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(" Error: plan.json not found. Run planner.py first.")
        return

    print(f" Received AI Plan: {data['summary']}\n")
    print(f"{'HOUR':<6} | {'REQUEST':<10} | {'STATUS':<25} | {'OUTPUT':<10}")
    print("-" * 60)

    for step in data['plan']:
        hour = step['hour']
        ai_req = step['total_kw']
        
        # 1. SEND TO HARDWARE (Simulation)
        hw_enforced, status_code = mock_fpga_hardware_gate(ai_req)
        
        # 2. DECODE HARDWARE STATUS
        status_msg = STATUS_MAP.get(status_code, "❓ UNKNOWN")
        
        # 3. PRINT STRUCTURED LOG
        print(f"{hour:<6} | {ai_req:<7} kW | {status_msg:<25} | {hw_enforced:<7} kW")
        
    print("-" * 60)
    print(" FINAL FPGA COMMANDS LATCHED FOR INVERTER.")

if __name__ == "__main__":
    run_safety_bridge()
