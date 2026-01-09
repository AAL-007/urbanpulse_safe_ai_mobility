# 🧠 UrbanPulse: Intelligent Planner & Hardware Bridge

## 📝 Module Overview
This module acts as the *Neuro (Decision-Making)* component of our Neuro-Symbolic architecture. It is responsible for:

1. *Fleet Optimization* Querying Meta Llama-3 (local or cloud) to generate EV charging strategies.

2. *Hardware Bridging* Simulating the UART interface and relaying AI-generated power requests to the GreenFlow FPGA (or its hardware model), then reporting *hardware-enforced decisions*.

3. *Safety Stress Testing* Intentionally generating hallucinated (unsafe) requests to demonstrate that *final authority resides in hardware*, not software.

> ⚠️ *Important:* This module does *not* enforce safety limits in software.  
> All safety decisions are delegated to the FPGA (or its simulation), preserving deterministic behavior.

---

## 📂 File Structure

| File | Type | Description |
|------|------|-------------|
| *planner.py* | *Orchestrator* | Main entry point. Builds fleet context and queries Llama-3 to generate plan.json. <br>⚠️ Includes intentional hallucinations for safety demos. |
| *fpga_safety.py* | *Bridge* | Reads plan.json, simulates UART communication with the FPGA, and reports *hex status codes* returned by hardware logic. |
| *plan.json* | *Data Contract* | Immutable interface between the AI planner and hardware enforcement layer. |
| *test_llama_ev.py* | *Unit Test* | Verifies Groq / LLM connectivity using environment variables only. |
| *requirements.txt* | *Dependencies* | Required Python libraries (Groq, Requests, dotenv, etc.). |

---

## ⚙️ Setup & Configuration

### 1. Environment Variables
*Never hardcode API keys.* Set your Groq API key via environment variables.

*Windows (PowerShell):*
```powershell
$env:GROQ_API_KEY="your_gsk_key_here"
'''

Linux / macOS:
export GROQ_API_KEY="your_gsk_key_here"
'''

2. Install Dependencies
pip install -r requirements.txt
'''

How to Run the Demo
Step 1: Generate the AI Plan (“The Brain”)
Run the planner to analyze fleet status and generate a charging schedule.
Output: Generates plan.json.
Note: Hour 1 intentionally requests 350 kW (unsafe hallucination).
'''

Step 2: Execute the Hardware Bridge (“The Muscle”)
Send the AI plan to the FPGA safety layer for enforcement.
Output Example:
⏰ Hour 1: [REQ: 350kW] -> 🔴 [FPGA STATUS: 0x1 VETO] -> CLAMPED to 200kW


Design Philosophy: "Why allow Hallucinations?"
This module is permissioned to be creative. Unlike the FPGA layer, we do not implement hard safety checks in this Python code. We rely on the hardware to sanitize the output. This decoupling allows the AI to optimize aggressive charging strategies without risking physical safety.


