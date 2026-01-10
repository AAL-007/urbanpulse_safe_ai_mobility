# Live Demo Explanation

## Purpose of the Demo

The live demo proves three things simultaneously:

1. The AI planner is real
2. The FPGA enforcement is real
3. Safety is physically enforced, not simulated in software

---

## Demo Setup

- Left terminal: AI Planner
- Right terminal: Integration Bridge (FPGA interface)
- Large font size for visibility
- No background windows

---

## Demo Sequence

### Step 1: Safe Request

- AI requests 200 kW
- FPGA evaluates request
- Status: OK
- Action: Approved

This shows normal operation.

---

### Step 2: Unsafe Request (Critical Moment)

- AI requests 350 kW
- FPGA evaluates request
- Status: HARDWARE VETO
- Action: CLAMPED to 200 kW

This is the key proof point.

The system does not warn.
It *enforces*.

---

### Step 3: Recovery

- AI requests a safe value again
- FPGA approves
- System returns to stable operation

---

## What the Red Text Means

When the terminal shows:

HARDWARE VETO ASSERTED

This indicates:
- A physical safety boundary was crossed
- Hardware intervened
- Unsafe power was blocked

This is not a log message.
It represents a hardware-level decision.

---

## Demo Conclusion

The demo demonstrates:

> AI can fail.  
> Hardware does not.  
> Safety is enforced before damage occurs.

This validates the core UrbanPulse architecture