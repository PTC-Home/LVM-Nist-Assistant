# NIST Logic Directory

> **Purpose:** Explains to a human user or future employee what the "Logic Base" is and how the AI interacts with it.

## 📂 Overview
This directory contains the core reasoning frameworks for the **LVM-Nist-Assistant**. While raw NIST PDFs provide the "what," the files here provide the "how"—instructing the AI on how to interpret technical data against federal standards.

---

## 📄 Key Files
* **NIST-Logic-Base.md**: The master reference document used by the AI's RAG system to map technical logs to specific NIST Control IDs.

---

> [!TIP]
> **Auditor Note:** This folder is monitored by Wazuh File Integrity Monitoring (FIM). Any changes to these logic files will immediately alter how the AI generates compliance reports.

> [!IMPORTANT]
> **AI Usage:** The local inference engine is configured to prioritize the definitions in `NIST-Logic-Base.md` when a conflict arises between raw documentation and local lab policy.


---
---


# NIST Logic Base (Master Reference)

> **Purpose:** The actual technical mapping and "bits of understanding" the AI pulls from during an audit.

## 🎯 Purpose
This document serves as the primary "Knowledge Bridge" for the **LVM-Nist-Assistant**. [cite_start]It defines the relationship between raw system telemetry and the NIST SP 800-53 / CSF 2.0 frameworks[cite: 1265].

---

## 🛠️ Interpretation Logic: Technical to NIST
When analyzing logs, the AI must follow these mapping priorities:

### 🛡️ Access Control (AC) Family
* **Telemetry:** Failed SSH attempts, unauthorized sudo requests.
* **NIST Mapping:** AC-2 (Account Management), AC-7 (Unsuccessful Logon Attempts).
* **Logic:** Any more than 3 failed attempts in 60 seconds triggers a `[!CAUTION]` flag.

### 📜 Audit & Accountability (AU) Family
* **Telemetry:** Wazuh agent disconnects, log deletion events.
* **NIST Mapping:** AU-2 (Event Logging), AU-6 (Audit Record Review).
* **Logic:** Missing telemetry windows trigger a `[!WARNING]` regarding audit trail continuity.

---

> [!TIP]
> **Tech-Savvy Lite Rule:** When a technical violation is found, the logic base requires the AI to explain the "Business Risk." For example, "A failed login isn't just a log entry; it's a potential door being kicked by an intruder."

> [!CAUTION]
> **Privacy Shield Enforcement:** This logic base strictly forbids the AI from requesting external data to verify a NIST control. All "Understanding" must be derived from the local files in `/Knowledge-Base`.
