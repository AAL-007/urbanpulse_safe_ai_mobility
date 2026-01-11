# UrbanPulse — Documentation

UrbanPulse is a *Neuro-Symbolic, Hardware-Enforced system* for safe intelligent electric mobility.

This documentation explains:
- What the system does
- Why it is needed
- How safety is guaranteed
- What the prototype demonstrates

UrbanPulse is designed for environments where *AI mistakes can cause physical damage* — such as EV depots, public transport infrastructure, and smart city systems.

---

## Core Idea (Plain Language)

AI systems are powerful, but they are *probabilistic*.  
Physical systems require *deterministic safety*.

UrbanPulse separates:
- *Intelligence* (AI planning)
- *Authority* (hardware enforcement)
- *Oversight* (human audit)

> AI may suggest.  
> Hardware decides.  
> Humans approve.

---

## Intent vs Reality

![Intent vs Reality][def]

The AI may request unsafe power levels.  
The hardware enforces the physically safe outcome.

---

## Documentation Map

- *Architecture* → architecture.md
- *Safety Model* → safety-model.md
- *Demo Walkthrough* → demo-walkthrough.md
- *Setup & Execution* → setup.md
- *Hardware Proofs* → hardware_proofs/

---

## What This Project Guarantees

- Deterministic hardware safety
- Bounded physical outputs
- Transparent monitoring
- Human-in-the-loop accountability

UrbanPulse does *not* promise perfect AI.  
It guarantees *safe outcomes even when AI is imperfect*.

[def]: assets/intent_vs_reality.jpeg