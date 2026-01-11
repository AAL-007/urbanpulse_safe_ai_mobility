# UrbanPulse
## A Neuro-Symbolic, Hardware-Enforced System for Safe Intelligent Electric Mobility

---

## 1. Introduction

*UrbanPulse* is a cyber-physical system designed to safely integrate artificial intelligence into electric mobility and charging infrastructure.

At its core, UrbanPulse answers a simple but critical question:

> *How do we safely use AI in systems where mistakes can cause real physical damage?*

UrbanPulse combines:

- AI-based decision making  
- Deterministic hardware enforcement  
- Transparent human oversight  

This ensures AI suggestions *never violate physical safety constraints*, even when AI behaves unpredictably.

---

## 2. The Problem We Are Solving

Modern AI systems (including large language models) excel at planning and optimization.  
However, they are *probabilistic*, not deterministic.

This creates risk when AI is used in real-world infrastructure:

- EV charging stations  
- Public transport depots  
- Smart traffic systems  
- Power-grid-connected devices  

### Core Risks

- AI systems can hallucinate  
- AI systems do not understand physics  
- AI systems cannot guarantee hard limits  

In software-only systems:

- Incorrect outputs may still execute  
- Safety checks can be bypassed  
- Failures are detected after damage  

In high-power environments, this leads to:

- Overloading  
- Thermal damage  
- Equipment failure  
- Fire hazards  

*UrbanPulse prevents unsafe actions before they happen.*

---

## 3. Design Philosophy

> **Intelligence suggests.  
> Authority enforces.**

This means:

- AI proposes actions  
- Hardware enforces physical limits  
- Humans observe and audit decisions  

Intelligence and control are intentionally separated.

---

## 4. High-Level Architecture

```text
AI Planner
   ↓
Integration Bridge
   ↓
FPGA Safety Gate
   ↓
Sentinel Monitor
```

Each layer has a single, clearly bounded responsibility.

---

## 5. Layer-by-Layer Breakdown

### 5.1 AI Planner (LLM Layer)

*Purpose*  
Generate optimized EV charging and mobility plans.

*Behavior*
- Analyzes fleet state and load  
- Uses an open-source LLM (e.g., Llama-3)  
- Outputs structured plans (plan.json)  

*Important*
- Does NOT enforce safety  
- May over-optimize or hallucinate  
- This is intentional  
- UrbanPulse assumes the AI can be wrong  

---

### 5.2 Integration Bridge (Software Transport)

*Purpose*  
Neutral transport between AI and hardware.

*Responsibilities*
- Read AI-generated plans  
- Forward raw requests to hardware  
- Receive and display enforced outcomes  

*Explicitly does NOT*
- Perform safety checks  
- Clamp values  
- Override hardware decisions  

This proves safety comes from *hardware*, not software.

---

### 5.3 GreenFlow FPGA Safety Gate (Hardware)

*Purpose*  
Physically enforce safety constraints.

*What it does*
- Runs deterministic Verilog logic  
- Checks every power request against:
  - Grid limits  
  - Thermal limits  
  - Fail-safe rules  
- Hardware-level clamping  
- Explicit status codes  

*Key Property*
- Clock-driven, deterministic logic  
- Cannot hallucinate  
- Cannot be overridden by software  

---

### 5.4 Sentinel Monitor (Oversight Layer)

*Purpose*  
Transparency and accountability.

*Functions*
- Monitor FPGA status outputs  
- Count violations  
- Log unsafe attempts  
- Raise alerts  

Ensures the system is *not a black box*.

---

## 6. Prototype Demonstration

### Failure Scenario (Intentional)

- AI requests *350 kW* (unsafe)  
- FPGA detects violation  
- Hardware asserts *VETO*  
- Power clamped to *200 kW*  
- Event logged by Sentinel  

### What This Proves
- AI planning is active  
- Hardware enforcement is real  
- Safety is physically guaranteed  

---

## 7. Beyond EV Charging

The same architecture applies to:

- Traffic-aware charging  
- Lane discipline enforcement  
- Battery health protection  
- Grid-aware scheduling  
- Smart city infrastructure  

Anywhere unsafe AI decisions can cause physical harm.

---

## 8. Human-in-the-Loop Design

UrbanPulse is *not fully autonomous by design*.

- Safety events are visible  
- Violations are logged  
- Decisions are auditable  
- Human oversight is mandatory  

This enables ethical deployment of AI in critical systems.

---

## 9. Guarantees and Limits

### Guarantees
- Deterministic safety enforcement  
- Bounded physical outputs  
- Hardware-level protection  
- Transparent monitoring  

### Non-Claims
- Zero failure  
- Perfect AI decisions  
- Fully autonomous control  

*Guarantee delivered:*  
Bounded, deterministic safety — even when AI is unpredictable.

---

## 10. Summary

UrbanPulse demonstrates a deployable model for safe AI in real-world infrastructure by combining:

- AI intelligence  
- Hardware authority  
- Human accountability  

This creates a system that is:
- Safer  
- More trustworthy  
- More realistic for real deployment  

---

## Final Principle

*AI assists.*  
*Hardware enforces.*  
*Humans approve.*