# LVM-Nist-Assistant: Hardened AI Auditing Environment

## 🛡️ Project Mission
The **LVM-Nist-Assistant** is a dual-machine, locally-hosted AI environment designed to perform autonomous and manual NIST compliance auditing. By utilizing a "Privacy Shield" architecture, this project ensures that sensitive security telemetry and audit data never leave the private network, fulfilling the highest standards of federal data sovereignty.

---

## 🌉 The "Privacy Shield" Architecture
This project leverages a hybrid hardware configuration to isolate the AI's "Brain" from the security lab's "Muscle."

* **Auditor Host (Legion 5):** Runs the hardened Ubuntu VM, Ollama Inference Engine, and Local RAG.
* **Security Stack (Desktop):** Hosts pfSense for network isolation and Wazuh for centralized log management.
* **The Bridge:** An encrypted Tailscale tunnel allows the AI to query security logs without exposing ports to the public internet.

---

## 📁 Repository Structure

| Folder | Contents |
| :--- | :--- |
| **`/infrastructure`** | Hardware mapping, pfSense rules, and the Wazuh-AI Bridge scripts. |
| **`/knowledge-base`** | Local NIST 800-53/CSF standards and the `NIST-Logic-Base.md`. |
| **`/prompts`** | Detailed Persona definitions for Manual vs. Automated auditing. |
| **`/reports`** | Drop zones for Automated Logs and Manual SAR templates. |
| **`/setup`** | Installation guides and CUDA configuration for the RTX 5060. |

---

## 🚀 Key Features

### 1. Dual-Persona Auditing
We utilize two distinct instruction sets to handle different operational tempos:
* **The Auditor:** A conversational consultant for manual NIST deep-dives.
* **The Night Watchman:** A clinical, low-latency persona for 24/7 automated alerting.

### 2. Tech-Savvy Lite Reporting
Every finding is translated into a business-risk summary, making technical security gaps understandable for leadership and stakeholders.

### 3. Visual Compliance Flags
Reports utilize GitHub Flavored Markdown (GFM) alerts for immediate status recognition.

---

## 🤝 Acknowledgments & Logical Partnership
This project was developed through a unique logical partnership with **Gemini (Google)**. 

Beyond serving as a technical tool, Gemini acted as a collaborative mind to think through the architectural challenges of this project. Through iterative feedback and mutual learning, we successfully bridged the gap between physical hardware isolation (Legion 5 vs. Desktop) and the rigorous requirements of the NIST framework. 

This partnership allowed for the creation of the **Privacy Shield** and the **Tech-Savvy Lite** reporting standard, achieving a level of organizational clarity and technical hardening that represents the future of secure AI implementation.

---

## ⚖️ Compliance Statement
This assistant is an **Audit Preparation Tool**. It is designed to support the **Human-in-the-Loop** protocol. Final compliance verification remains the responsibility of the designated Security Officer.

---

**Built with 🛡️ Privacy and 🧠 Intelligence in 2026.**
