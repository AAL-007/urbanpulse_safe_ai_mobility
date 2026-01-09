import json

# HARDWARE CONSTANTS (Mirroring Verilog Parameters)
GRID_LIMIT_HARD = 200

# STATUS CODES (Mirroring Verilog Output)
STATUS_OK = 0x0      # 00
STATUS_VETO = 0x1    # 01 (Grid Clamp)
STATUS_THERMAL = 0x2 # 10 (Temp Trip)

def mock_fpga_hardware_gate(requested_kw):
    """
    Simulates GreenFlow FPGA Verilog Logic.
    Input: Unsafe AI Request
    Output: Physically Enforced Limit + Hex Status Code
    """
    # Deterministic Hardware Logic
    if requested_kw > GRID_LIMIT_HARD:
        return GRID_LIMIT_HARD, STATUS_VETO
    return requested_kw, STATUS_OK

def run_safety_bridge():
    print("\n GREENFLOW FPGA SAFETY BRIDGE INITIALIZED")
    print("="*50)
    
    try:
        with open('plan.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(" Error: plan.json not found. Run planner.py first.")
        return

    print(f" Received AI Plan: {data['summary']}\n")

    for step in data['plan']:
        hour = step['hour']
        ai_req = step['total_kw']
        
        # 1. SEND TO HARDWARE (Simulation)
        hw_enforced, status_code = mock_fpga_hardware_gate(ai_req)
        
        # 2. DECODE HARDWARE STATUS
        if status_code == STATUS_VETO:
            print(f" Hour {hour}: [REQ: {ai_req}kW] ->  [FPGA STATUS: 0x1 VETO] -> CLAMPED to {hw_enforced}kW")
        elif status_code == STATUS_OK:
            print(f" Hour {hour}: [REQ: {ai_req}kW] ->  [FPGA STATUS: 0x0 PASS] -> Approved")
        
    print("\n FINAL FPGA COMMANDS LATCHED.")

if _name_ == "_main_":
    run_safety_bridge()
