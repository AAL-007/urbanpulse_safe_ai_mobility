import json

# Read LLM plan
with open('plan.json', 'r') as f:
    plan = json.load(f)

print("🔋 LLM EV PLANNING SYSTEM LIVE")
print("=" * 50)

GRID_LIMIT = 200  # kW
FPGA_COMMANDS = []

for hour_plan in plan['plan']:
    hour = hour_plan['hour']
    total_kw = hour_plan['total_kw']
    
    # SAFETY CHECK 1: Grid limit
    if total_kw > GRID_LIMIT:
        print(f"🚨 HOUR {hour} REJECTED: {total_kw}kW > {GRID_LIMIT}kW")
        fpga_cmd = {"hour": hour, "status": "REJECTED", "reason": "GRID_OVERLOAD"}
    else:
        # SAFETY CHECK 2: Per-bus limits
        if hour_plan['bus1_kw'] > 75 or hour_plan['bus2_kw'] > 75 or hour_plan['bus3_kw'] > 75:
            print(f"⚠️ HOUR {hour} CLIPPED: Bus power too high")
            # Clip to safe limits
            safe_bus1 = min(hour_plan['bus1_kw'], 75)
            safe_bus2 = min(hour_plan['bus2_kw'], 75) 
            safe_bus3 = min(hour_plan['bus3_kw'], 75)
            total_safe = safe_bus1 + safe_bus2 + safe_bus3
            print(f"   → Safe: b1={safe_bus1}, b2={safe_bus2}, b3={safe_bus3}kW")
            fpga_cmd = {
                "hour": hour, "status": "CLIPPED", 
                "bus1_kw": safe_bus1, "bus2_kw": safe_bus2, "bus3_kw": safe_bus3,
                "total_kw": total_safe
            }
        else:
            print(f"✅ HOUR {hour} APPROVED: {total_kw}kW → {hour_plan['notes']}")
            fpga_cmd = hour_plan.copy()
            fpga_cmd["status"] = "APPROVED"
    
    FPGA_COMMANDS.append(fpga_cmd)

print("\n🎯 FPGA COMMANDS READY:")
print(json.dumps(FPGA_COMMANDS, indent=2))
print(f"\n📊 Summary: {plan['summary']}")
