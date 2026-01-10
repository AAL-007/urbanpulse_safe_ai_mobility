# LLM Planner Overview

## Purpose of the AI Planner

The AI planner in UrbanPulse is responsible for *optimization*, not safety.

Its role is to:
- Analyze fleet requirements
- Optimize charging schedules
- Maximize throughput and efficiency
- Suggest power requests

It is intentionally treated as an *untrusted component*.

---

## Why Use an LLM?

Large language models are powerful at:
- Pattern recognition
- Multi-objective optimization
- Scenario reasoning

However, they are also:
- Probabilistic
- Non-deterministic
- Capable of hallucination

UrbanPulse embraces this reality instead of hiding it.

---

## Hallucination Is a Feature Here

In this project:
- The AI planner is allowed to over-request power
- Unsafe outputs are intentionally demonstrated
- Example: requesting 350 kW when only 200 kW is safe

This proves a key point:

> *System safety does not depend on AI correctness.*

---

## Planner Output Format

The planner outputs a structured plan (JSON) containing:
- Requested power per time slot
- Scheduling decisions
- Metadata for evaluation

This output is passed verbatim to the FPGA layer.

No filtering is applied in software.

---

## What the Planner Cannot Do

The AI planner:
- Cannot bypass hardware rules
- Cannot disable safety checks
- Cannot override FPGA logic
- Cannot affect final power delivery directly

---

## Design Philosophy

The planner is allowed to be:
- Creative
- Aggressive
- Imperfect

Because it is *never trusted with authority*.

This separation is fundamental to UrbanPulse.
