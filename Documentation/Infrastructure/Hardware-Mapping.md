# Hardware Allocation

### Hardware Allocation Mapping

## 🛡️ Infrastructure Overview
This project utilizes a dual-machine architecture to ensure the **LVM-Nist-Assistant** remains isolated from high-intensity laboratory traffic. [cite_start]This physical separation provides a hybrid "Air-Gapping" logic, ensuring the Auditor Persona remains functional and secure even if the primary security lab is under heavy load or compromised[cite: 209, 210, 227].

---

## 💻 The Auditor (Legion 5 Laptop Host)
[cite_start]The laptop serves as the dedicated "Compliance Station" for running the mid-tier AI model[cite: 205, 207].

* **Processor:** AMD Ryzen 7
    * [cite_start]**Allocation:** 4 vCPUs assigned to the AI Virtual Machine[cite: 190, 252].
    * [cite_start]**NPU Offloading:** The dedicated NPU will handle background OS tasks, leaving the GPU entirely for deep NIST analysis[cite: 211, 267].
* [cite_start]**Graphics (NVIDIA RTX 5060):** * **Memory:** 8GB GDDR7 VRAM[cite: 212].
    * [cite_start]**Configuration:** Dedicated to the AI VM via GPU Passthrough[cite: 221, 253].
* [cite_start]**System RAM:** 16GB dedicated to the AI VM to ensure stability during document ingestion[cite: 167, 254].
* [cite_start]**Storage:** 50GB SSD for fast access to model weights and the NIST RAG library[cite: 181].

---

## 🖥️ The Security Stack (Main Desktop Host)
[cite_start]The desktop manages the foundational security services and network monitoring[cite: 251, 255].

* [cite_start]**Primary Services:** * **pfSense:** Manages the isolated VLAN and enforces "Zero Egress" rules for the laptop's AI[cite: 170, 259].
    * [cite_start]**Wazuh Manager:** Collects and processes logs from the laptop-based Wazuh Agent[cite: 172, 255].
* **Connectivity:**
    * [cite_start]**Tailscale:** Creates an encrypted "Tailnet" bridge to allow secure access to the Wazuh dashboard from the laptop[cite: 231, 261].

---









