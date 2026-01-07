@echo off
:loop
echo 🔥 LIVE EV PLANNER RUNNING...
python fpga_safety.py
timeout /t 300
goto loop
