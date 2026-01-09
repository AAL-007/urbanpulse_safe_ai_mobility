@echo off
:loop
cls
echo ==================================================
echo 🔥 URBANPULSE LIVE DEMO: ORCHESTRATION CYCLE START
echo ==================================================

echo.
echo [STEP 1] 🧠 AI BRAIN: Generating New Fleet Plan...
python planner.py

echo.
echo [STEP 2] 🛡️ HARDWARE MUSCLE: Verifying Safety...
python fpga_safety.py

echo.
echo ✅ Cycle Complete. System Sleeping...
timeout /t 300
goto loop
