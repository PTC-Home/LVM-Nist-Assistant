# Integration Overview: Wazuh & AI Auditor

## 🌉 The Automation Bridge
This integration creates a functional link between **Wazuh** (the "Eyes" of the system) and the **LVM-Nist-Assistant** (the "Brain"). By automating the flow of security telemetry into the AI inference engine, we transform a passive monitoring system into an active compliance auditor.

---

## 🛡️ Why This Integration is Important

### 1. Data Privacy (The Privacy Shield)
Traditionally, AI analysis requires sending logs to external cloud providers. This bridge keeps all sensitive NIST audit data within our isolated VLAN. Logs are pulled via a local Tailscale tunnel, analyzed by a local 8B model, and stored locally.

### 2. Operational Efficiency
Manual NIST auditing is slow. This integration allows for:
* **Real-Time Mapping:** Instantly associating a technical alert with a NIST Control ID.
* **Noise Reduction:** Using Regex to filter out "fluff" and only sending high-fidelity security signals to the AI.

### 3. Knowledge Bridging
It solves the "Specialist Gap." By instructing the AI to output in **Tech-Savvy Lite**, we ensure that even complex security events are understandable for stakeholders who may not be NIST experts.

---

## 🚀 Capabilities & Outcomes

| Feature | Achievement |
| :--- | :--- |
| **Automated Log Extraction** | Pulls Level 12+ alerts directly from the Wazuh API without human intervention. |
| **NIST Control Mapping** | The AI identifies which specific SP 800-53 or CSF control was triggered by the event. |
| **Visual Reporting** | Automatically utilizes GitHub-style callouts to flag critical risks and positive outcomes. |

---

> [!TIP]
> **Security Outcome:** This bridge allows the Wazuh Manager to trigger the AI even when you are away from your desk, ensuring that "Compliance Snapshots" are ready and waiting for review every morning.

> [!WARNING]
> **Universal Compliance Requirement:** Automation does not replace human oversight. The Auditor Persona is designed to assist in "Audit Preparation"; final verification of compliance must always be performed by a human-in-the-loop to meet NIST standards.

> [!CAUTION]
> **Privacy Shield Reminder:** Ensure the `Wazuh-AI-Integration.py` script credentials are never committed to the public GitHub repository. Use environment variables or a local `.env` file to protect the Wazuh API keys.

---
