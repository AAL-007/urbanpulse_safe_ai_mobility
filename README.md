# UrbanPulse - Safe AI Mobility Platform 
## 🏗️ Architecture Strategy: Why "Hardware-Enforced"?

UrbanPulse is not just a software planner. It is a *Cyber-Physical Safety System* designed to operate safely under the Stability Trilemma of Urban EV Infrastructure.

### The Problem
Generative AI (LLMs) enables creative, context-aware optimization (e.g., “Charge more because demand is dropping”).  
However, LLMs are probabilistic systems—they can *hallucinate unsafe commands*.

In a high-power EV depot (hundreds of kW to MW scale), a hallucination is not just a wrong answer—it is a *thermal, electrical, and fire hazard*.

### Our Solution: "Trust but Verify"
UrbanPulse uses a *Neuro-Symbolic, Hardware-Enforced Architecture*:

1. *The Brain (Software – LLM Planner)*  
   Meta Llama-3 generates charging strategies using fleet state, tariffs, and forecasts.  
   It is intentionally allowed to be creative—and therefore, occasionally wrong.

2. *The Muscle (Hardware – GreenFlow FPGA)*  
   A deterministic FPGA (Verilog) sits physically between the AI and the charging hardware.
   - Enforces immutable limits (grid cap, per-bus current, thermal thresholds)
   - Executes cycle-accurate logic
   - *Cannot be overridden by software, prompts, or API responses*

### Result
The AI proposes a Strategy.  
The FPGA enforces the Truth.

This guarantees that even if the AI hallucinates an unsafe request, *the physical system remains within safe operating limits*.
