#Click Setup
REM 1. Install dependencies (one-time)
pip install groq python-dotenv requests

REM 2. Generate 24hr plan
python planner.py

REM 3. Start LIVE system (runs forever)
run.bat


# Generate plan(planner.py)
✅ plan.json CREATED SUCCESSFULLY!
📊 Hours planned: 24
⚡ Hour 0: 150kW (Charge low-SoC buses 1&3)
🎯 Ready for fpga_safety.py!


#Safety Check (fpga_safety.py)
🚨 HOUR 0 REJECTED: 200kW > 200kW
✅ HOUR 1 APPROVED: 175kW → Continue bus1, start bus2
🎯 FPGA COMMANDS READY


#Live Loop (run.bat)
🔥 LIVE EV PLANNER RUNNING... (5min intervals)


