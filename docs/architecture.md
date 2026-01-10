# UrbanPulse System Architecture

## Overview

UrbanPulse is a safety-first AI–hardware system designed for electric mobility infrastructure such as EV depots, public transport charging hubs, and smart city power control points.

The core idea is simple:

> **AI is allowed to think.  
> Hardware is allowed to decide.**

Instead of trusting AI outputs directly, UrbanPulse enforces all physical actions through deterministic FPGA logic.

---

## High-Level Architecture

UrbanPulse is composed of three clearly separated layers:

1. *AI Planner (Intelligence Layer)*
2. *FPGA Safety Controller (Authority Layer)*
3. *Sentinel Monitor (Oversight & Audit Layer)*

Each layer has a single responsibility and no hidden authority.

---

## 1. AI Planner (LLM-Based Intelligence)

- Implemented using a large language model (Llama-based)
- Optimizes charging schedules, power requests, and fleet behavior
- Operates in *probabilistic space*
- Can over-optimize or hallucinate by design

The AI planner *does not*:
- Control hardware directly
- Bypass safety rules
- Override physical limits

---

## 2. GreenFlow FPGA Controller (Deterministic Enforcement)

This is the core safety component.

- Implemented in Verilog
- Runs on FPGA logic (or simulated FPGA)
- Receives raw power requests from AI via UART
- Applies fixed, deterministic safety rules:
  - Grid limits
  - Thermal limits
  - Hard-coded safety boundaries

The FPGA outputs:
- Approved power
- Or a clamped, safe power value
- Or a veto signal

This logic is:
- Deterministic
- Non-probabilistic
- Immune to AI hallucinations

---

## 3. Sentinel Monitor (Audit & Oversight)

The Sentinel module monitors all enforcement actions:

- Detects unsafe transitions
- Raises live alerts
- Latches historical violations
- Counts safety violations

This enables:
- Post-event audits
- Human review
- Compliance verification

---

## Data Flow Summary

1. AI proposes an action (e.g., 350 kW)
2. Request passes to FPGA
3. FPGA evaluates safety
4. Unsafe requests are clamped or vetoed
5. Sentinel logs and signals violations
6. Only safe power reaches the system

---

## Architectural Principle

UrbanPulse deliberately rejects “AI-in-the-loop” control.

Instead, it implements:

> **AI-in-the-loop planning,  
> Hardware-in-the-loop enforcement,  
> Human-in-the-loop approval.**

This makes the system suitable for safety-critical, real-world deployment.