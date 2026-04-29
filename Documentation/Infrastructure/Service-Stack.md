# Service Stack & Software Layers

## 🛡️ The Hardened Foundation
This document lists the specific software layers and services that make the **LVM-Nist-Assistant** functional while maintaining the **Privacy Shield**. Documenting these versions is critical for your "Save Game" if the environment needs to be rebuilt.

---

## 💻 Auditor VM (Laptop-Side)
The following services run on the Legion 5 dedicated AI Virtual Machine.

### 1. Operating System
* **Distro:** Ubuntu 26.04 LTS (Hardened Kernel).
* **Role:** Primary host for the AI Inference Engine and Local RAG.

### 2. AI Inference Engine
* **Service:** Ollama (version 0.5.x or higher).
* **Model:** 8B parameter model (e.g., Llama 3.3).
* **Quantization:** 8-bit (for precision) or 4-bit (for speed).
* **Local API Port:** `11434` (Strictly restricted by UFW).

### 3. Local Security Services
* **Wazuh Agent:** Installed to monitor internal AI system logs.
* **File Integrity Monitoring (FIM):** Active on the `/knowledge-base` folder.
* **UFW (Uncomplicated Firewall):** Configured for "No Egress" status.

---

## 🖥️ Security Stack (Desktop-Side)
The following services are hosted on the main desktop to provide orchestration and monitoring.

### 1. Networking & Perimeter
* **pfSense:** Managing the isolated VLAN and Tailscale Subnet Routing.
* **Tailscale:** Encrypted bridge between the laptop and desktop environments.

### 2. Centralized Monitoring
* **Wazuh Manager:** Collects log evidence from the Auditor VM.
* **Wazuh Dashboard:** Web interface for viewing compliance alerts.

---

## 🚀 Automation & Bridge Services
These scripts facilitate the communication between Wazuh and the AI.

* **Log Extractor:** Python script utilizing the Wazuh API to pull technical logs.
* **NIST Mapper:** Local script that feeds filtered logs into the AI for automated NIST control mapping.

> [!TIP]
> **Security Outcome:** By separating the AI Inference Engine (Laptop) from the Monitoring Stack (Desktop), we ensure that high-intensity AI tasks do not interfere with real-time security alerting.

> [!CAUTION]
> **Universal Compliance Requirement:** All services must be configured to communicate only over the private Tailscale tunnel. Any attempt by a service to reach a public IP must be blocked and logged by pfSense.
