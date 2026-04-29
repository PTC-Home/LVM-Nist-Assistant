# Knowledge Base: The NIST Brain

## 🧠 Overview
This folder serves as the central repository for the compliance standards and technical filters used by the **LVM-Nist-Assistant**. [cite_start]By storing these rules locally, we ensure that the AI provides evidence-based analysis while maintaining total data privacy[cite: 1258, 1261, 1308].

---

## 📂 Core Components

### 1. NIST Standards Library
[cite_start]This section contains the official "Rulebooks" the AI uses to measure compliance[cite: 1259, 1300].
* [cite_start]**NIST SP 800-53 Rev. 5:** Granular security and privacy controls for federal systems[cite: 1259].
* [cite_start]**NIST CSF 2.0:** High-level framework for managing and communicating cybersecurity risk[cite: 1259].

### 2. Regex Library (`Regex-Library.md`)
[cite_start]While the AI understands the "meaning" of your logs, this library provides the **Surgical Precision** needed to find exact technical evidence.
* [cite_start]**Log Filtering:** Pre-processes massive SIEM logs to extract only relevant "security signals" like failed login attempts or unauthorized IPs[cite: 1277].
* [cite_start]**PII Stripping:** Automatically redacts sensitive information before analysis to enforce the Privacy Shield[cite: 1278].

---

## 🛡️ The Local RAG Protocol
This assistant utilizes **Retrieval-Augmented Generation (RAG)**. [cite_start]Instead of guessing based on general training, the AI is forced to look at the specific files in this folder to provide audit answers[cite: 1260, 1261].

> [!TIP]
> **Audit Consistency:** Storing standards here ensures that the AI never "hallucinates" a rule. [cite_start]It provides consistent evidence mapping every time you run a report[cite: 1261].

> [!CAUTION]
> **Data Integrity:** Any changes to the files in this folder will affect the AI's auditing logic. [cite_start]Use the Wazuh **File Integrity Monitoring (FIM)** guide in `/infrastructure` to watch this folder for unauthorized changes[cite: 1270, 1301].

---

## 🚀 How to Add New Knowledge
1. [cite_start]Place a `.pdf` or `.json` version of a security standard into this folder[cite: 1259].
2. [cite_start]Update your **Local RAG Config** to include the new file path[cite: 1260].
3. [cite_start]Re-index the model so the AI "learns" the new controls[cite: 1301].
