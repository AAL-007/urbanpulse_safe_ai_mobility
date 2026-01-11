# Prototype Demonstration Walkthrough

This prototype intentionally demonstrates an *unsafe AI scenario*.

---

## Step-by-Step Demo

1. AI planner generates a charging plan
2. Plan includes an unsafe request (350 kW)
3. Raw request is sent to hardware
4. FPGA detects violation
5. Hardware asserts veto
6. Power is clamped to 200 kW
7. Event is logged

---

## Live Evidence

![Hardware Veto][def]

This output shows:
- Unsafe AI request
- Hardware veto
- Enforced safe power

This is *physical enforcement*, not software correction.

---

## What This Proves

- AI planning is active
- Hardware enforcement is real
- Safety is guaranteed before execution

[def]: assets/red_veto_terminal.jpeg