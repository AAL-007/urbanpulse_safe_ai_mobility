UrbanPulse
A Neuro-Symbolic, Hardware-Enforced System for Safe Intelligent Electric Mobility
1. Introduction
UrbanPulse is a cyber-physical system designed to safely integrate artificial intelligence into electric mobility and charging infrastructure.
At its core, UrbanPulse answers a simple but critical question:
How do we safely use AI in systems where mistakes can cause real physical damage?
The project combines:
AI-based decision making
Deterministic hardware enforcement
Transparent human oversight
to ensure that AI suggestions never violate physical safety constraints, even if the AI behaves unpredictably.
2. The Problem We Are Solving
Modern AI systems (including large language models) are powerful at planning and optimization.
However, they are probabilistic, not deterministic.
This creates a serious risk when AI is used in real-world infrastructure, such as:
EV charging stations
Public transport depots
Smart traffic systems
Power-grid connected devices
The Core Risk
AI systems can hallucinate
AI systems do not understand physics
AI systems cannot guarantee hard limits
In software-only systems:
A wrong AI output may still be executed
Safety checks can be bypassed
Failures happen after damage occurs
In high-power environments, this can lead to:
Overloading
Thermal damage
Equipment failure
Fire hazards
UrbanPulse is designed to prevent unsafe actions before they happen, not just detect them afterward.
3. Design Philosophy (In Plain Language)
UrbanPulse is built on one guiding principle:
Intelligence should suggest.
Authority should enforce.
This means:
AI can propose actions
Hardware decides what is physically allowed
Humans can observe and audit decisions
The system intentionally separates intelligence from control.
4. High-Level Architecture Overview
UrbanPulse consists of four main layers:
Copy code

AI Planner  →  Integration Bridge  →  FPGA Safety Gate  →  Sentinel Monitor
Each layer has a clear, limited responsibility.
5. Layer-by-Layer Explanation
5.1 AI Planner (LLM Layer)
Purpose:
Generate optimized plans for EV charging and mobility decisions.
What it does:
Analyzes fleet state, load, and constraints
Uses an open-source LLM (e.g., Llama-3)
Produces a structured plan (plan.json)
Important:
The AI planner does not enforce safety.
It may:
Over-optimize
Make aggressive suggestions
Hallucinate unsafe values (intentionally demonstrated)
This is a design choice, not a flaw.
UrbanPulse assumes the AI can be wrong.
5.2 Integration Bridge (Software Transport Layer)
Purpose:
Act as a neutral messenger between AI and hardware.
What it does:
Reads AI-generated plans
Sends raw requests to hardware (real or simulated)
Receives hardware responses
Displays enforced outcomes
What it does NOT do:
No safety logic
No clamping
No corrections
No overrides
This layer exists to prove that safety decisions come from hardware, not software.
5.3 GreenFlow FPGA Safety Gate (Hardware Layer)
Purpose:
Physically enforce safety constraints.
What it does:
Runs deterministic Verilog logic
Checks every power request against:
Grid limits
Thermal limits
Fail-safe rules
Generates explicit status codes
Clamps unsafe values at the hardware level
Key property:
This logic is clock-driven, deterministic, and cannot hallucinate.
Once deployed, software cannot override it.
5.4 Sentinel Monitor (Oversight & Accountability Layer)
Purpose:
Observe and record safety interventions.
What it does:
Monitors FPGA status outputs
Counts violations
Raises alerts
Logs unsafe attempts
Enables audit and review
This layer enables:
Transparency
Human oversight
System accountability
It ensures the system is not a “black box”.
6. What the Prototype Demonstrates
The prototype intentionally demonstrates a failure scenario.
Demonstration Scenario
AI requests 350 kW (unsafe)
Hardware detects violation
FPGA asserts a VETO
Power is clamped to 200 kW
Event is logged by Sentinel logic
This proves:
AI planning is active
Hardware enforcement is real
Safety is physically guaranteed
7. Beyond Charging: Smart Mobility Scope
Although the prototype focuses on EV charging safety, the architecture supports broader use cases:
Traffic-aware charging control
Lane discipline enforcement
Battery health protection
Grid-aware scheduling
Smart city integration
The same AI + hardware enforcement model can be applied wherever unsafe AI decisions could cause physical harm.
8. Human-in-the-Loop Philosophy
UrbanPulse is not fully autonomous by design.
Humans remain part of the system:
Safety events are logged
Violations are visible
Decisions are auditable
Oversight is possible
This ensures ethical deployment of AI in critical systems.
9. What UrbanPulse Guarantees (and What It Doesn’t)
Guarantees
Deterministic safety enforcement
Bounded physical outputs
Hardware-level protection
Transparent monitoring
Does NOT Claim
Zero failure
Perfect AI decisions
Fully autonomous control
Instead, UrbanPulse guarantees:
Bounded, deterministic safety — even when AI behaves unpredictably.
10. Summary
UrbanPulse demonstrates a practical, deployable model for integrating AI into real-world infrastructure safely.
By combining:
AI intelligence
Hardware authority
Human accountability
it creates a system that is:
Safer
More trustworthy
More realistic for real deployment
Final Principle
AI assists.
Hardware enforces.
Humans approve.

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
