# Safety Model & Enforcement Logic

UrbanPulse enforces safety using *deterministic hardware*, not software heuristics.

---

## Safety Logic Overview

![Hardware Control Flow][def2]

All AI requests pass through the FPGA safety gate.

### Safety Checks (Hardware-Enforced)

1. Grid power limit
2. Thermal threshold
3. Fail-safe conditions
4. AI heartbeat validity

---

## Status Codes

| Code | Meaning        |
|----|---------------|
| 00 | OK (Approved) |
| 01 | Grid Veto     |
| 10 | Thermal Trip  |
| 11 | AI Fault     |

---

## Deterministic Enforcement

- Logic executes on clock edges
- No floating states
- No probabilistic behavior
- No software override

This ensures *bounded physical behavior*.

---

## Power & Efficiency Evidence

![Power Summary][def]

The FPGA safety logic operates at *very low power* while enforcing hard physical limits.

---

## Hardware Verification

Raw engineering evidence is available in:

docs/hardware_proofs/

This includes:
- Vivado waveforms
- Synthesis summaries
- Power reports
- AI hallucination inputs

These files are provided for *verification and audit*, not marketing.

[def]: assets/power_summary.jpeg
[def2]: assets/hardware_control_flow.jpeg