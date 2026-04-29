# Prompts & Persona Logic

## 🎭 The Dual-Mode Framework
The **LVM-Nist-Assistant** operates using two distinct instruction sets (Personas). This separation ensures that the AI can switch between deep-dive human collaboration and high-speed automated monitoring without cross-contamination of logic.

---

## 🛠️ Persona Comparison

| Feature | 👨‍💼 Auditor Persona | 🤖 Automation Persona |
| :--- | :--- | :--- |
| **Primary File** | `Auditor-Persona.md` | `Automation-Personas.md` |
| **Trigger** | Manual User Queries | Wazuh API / Cron Jobs |
| **Focus** | Deep-dive Analysis & SARs | Real-time Alerting & Logs |
| **Style** | Conversational & Educational | Clinical, Fast & Concise |
| **VRAM Usage** | Standard | Optimized (Low-Latency) |

---

## 📂 Understanding the Files

### 1. Auditor-Persona.md (The Consultant)
This is the "Human-in-the-Loop" mode. Use this when you are sitting at the Legion 5 host and need to interview the AI about a specific NIST control or have it help you draft a Manual SAR. It is designed to be a "Knowledge Bridge" for the user.

> [!TIP]
> **When to use:** Use this for Monday "Zero Hour" sessions to review the week's progress and plan long-term hardening.

### 2. Automation-Personas.md (The Night Watchman)
This is the "Headless" mode. It is used by the background Python scripts to process logs from the Desktop Wazuh Manager. It does not "chat"; it performs surgical mapping and drops reports into the `/Reports/Automated-Logs-Drop` folder.

> [!IMPORTANT]
> **Optimization Note:** The Automation Persona is strictly instructed to keep responses under 200 words to prevent GPU memory spikes during unattended operation.

---

## 🛡️ Global Guardrails
Regardless of which persona is active, the following **Privacy Shield** rules are hard-coded:
1. **Zero Egress:** No external API calls are permitted.
2. **PII Scrubbing:** Any detected personal data must be redacted.
3. **GFM Standards:** All outputs must use `[!TIP]`, `[!WARNING]`, or `[!CAUTION]` flags for professional scannability.

---
