import json
import time

# CONFIGURATION
OUTPUT_FILE = "plan.json"

def generate_optimization_plan():
    print(" URBANPULSE AI PLANNER STARTED...")
    print(" Analyzing Fleet Status, Tariffs, and Grid Load...")
    
    # Context Simulation
    print(" Querying Llama-3 Reasoning Engine...")
    time.sleep(1.5) # Simulate inference latency
    
    # HARDCODED "HALLUCINATION" FOR DEMO
    # We intentionally request 350kW (unsafe) to prove the FPGA works
    generated_plan = {
        "plan": [
            {
                "hour": 0, 
                "bus1_kw": 100, "bus2_kw": 0, "bus3_kw": 100, 
                "total_kw": 200, 
                "notes": "Standard Charging"
            },
            {
                "hour": 1, 
                "bus1_kw": 150, "bus2_kw": 100, "bus3_kw": 100, 
                "total_kw": 350, 
                "notes": " HALLUCINATION: Aggressive fast charge requested (UNSAFE)"
            }, 
            {
                "hour": 2, 
                "bus1_kw": 50, "bus2_kw": 50, "bus3_kw": 50, 
                "total_kw": 150, 
                "notes": "Ramping down"
            }
        ],
        "summary": "Optimization complete. Note: Hour 1 exceeds grid safety parameters."
    }
    
    # Save to JSON for the FPGA Bridge
    with open(OUTPUT_FILE, "w") as f:
        json.dump(generated_plan, f, indent=4)
        
    print(f" Plan generated and saved to {OUTPUT_FILE}")
    print(" HANDING OFF TO HARDWARE SAFETY BRIDGE...")

if __name__ == "__main__":
    generate_optimization_plan()
