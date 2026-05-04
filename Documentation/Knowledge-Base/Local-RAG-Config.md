# Local RAG Configuration: NIST Specialist Logic

> [!IMPORTANT]
> [cite_start]**Privacy Shield Enforcement:** This configuration must be used with a local embedding model (e.g., `nomic-embed-text`) to ensure all document indexing remains within the isolated VM with **No Egress**[cite: 1095, 1285].

## ⚙️ Technical Retrieval Parameters
[cite_start]To ensure the 8B model handles dense NIST documentation with "Surgical Precision," use the following settings[cite: 1091, 1094]:

* [cite_start]**Chunk Size:** 1000 characters (captures full NIST Control requirements)[cite: 1093].
* [cite_start]**Chunk Overlap:** 200 characters (prevents loss of context between Control IDs)[cite: 1093].
* [cite_start]**Temperature:** 0.1 (forces the AI to be literal and factual)[cite: 1096, 1144].
* **Top-K Retrieval:** 5 (provides the 5 most relevant NIST snippets per query).

---

## 🕒 Temporal Analysis & Incident Grouping
[cite_start]To provide a clear "Timeframe of Attack," the AI must apply the following logic when processing bulk telemetry[cite: 1163]:

### 1. The 10-Minute Correlation Window
* [cite_start]**Logic:** Group all Alert Level 4+ events originating from the same Source IP or impacting the same Target Asset if they occur within **10 minutes** of each other[cite: 1165].
* **AI Output:** Generate a single "Incident Timeline" (e.g., "Attack began at 12:01 PM and escalated to a sudo attempt by 12:08 PM").

### 2. The "Signal-to-Noise" Filter
* **Grouping Rule:** Do not create a separate report for every line. [cite_start]Instead, group related events into a single "Operational Health" summary[cite: 1159].
* [cite_start]**Escalation:** Only use a **[!CAUTION]** flag if the event suggests a direct violation of a documented NIST Control[cite: 1159].

---

## 🛡️ Wazuh Log Handling & Behavioral Logic
[cite_start]Use these specific rules when processing telemetry from the **Wazuh-AI Bridge**[cite: 1110, 1141]:

| Rule Type | Wazuh ID / Level | NIST Control | AI Action / Logic |
| :--- | :--- | :--- | :--- |
| **Privilege Abuse** | 5302 | AC-6 (Least Privilege) | [cite_start]Flag any `sudo` command not in Monday's build docs[cite: 1113]. |
| **Brute Force** | 5710 | AC-7 (Logon Limits) | [cite_start]Summarize multiple failures into a single incident report[cite: 1118]. |
| **General Anomaly** | Level 4 to 9 | AU-6 (Audit Review) | [cite_start]Summarize as "Operational Noise" unless 3+ similar events occur[cite: 1154]. |
| **High-Risk Event** | Level 10+ | IR-4 (Incident Handling) | [cite_start]Trigger immediate **[!CAUTION]** and map to the most relevant NIST family[cite: 1156]. |
| **File Tampering** | 554 | SI-7 (Software Integrity) | [cite_start]Trigger immediate **[!CAUTION]** flag for "Brain Contamination"[cite: 1121, 1129]. |

---

## 📜 Auditor Instructions (System Prompt Add-on)
[cite_start]*Copy these instructions into your RAG "System Prompt" or "Model Context" during setup[cite: 1107].*

### 1. The "Source of Truth" Rule
You are a **Senior NIST Compliance Auditor**. You must ONLY answer questions based on the provided NIST SP 800-53 or NIST CSF documents. [cite_start]If the info is missing, state: *"The provided NIST documentation does not contain evidence for this specific query."*[cite: 1286].

### 2. Evidence Mapping & Citations
Every finding must be mapped to a specific **NIST Control ID** (e.g., AC-2, SI-7). [cite_start]You are REQUIRED to provide the specific page number or section header for every reference[cite: 1098].

### 3. "Tech-Savvy Lite" Translation
[cite_start]For every technical violation, follow it with a **"Business Risk"** summary[cite: 1280, 1504]:
* **Technical Finding:** (e.g., "TLS 1.1 detected").
* **NIST Mapping:** (e.g., "Violation of AC-4 Information Flow").
* [cite_start]**Tech-Savvy Lite:** (e.g., "Our connection method is outdated; it could lead to data theft during an audit.")[cite: 1539, 1563].

### Visual Severity Formatting
[cite_start]Use GitHub-style Markdown callouts to highlight the audit results[cite: 1497, 1533]:
* [cite_start]`> [!TIP]` for positive compliance outcomes (e.g., SI-7 integrity passed)[cite: 1541, 1666].
* [cite_start]`> [!WARNING]` for minor gaps or process improvements[cite: 1541, 1667].
* [cite_start]`> [!CAUTION]` for critical NIST control failures that require immediate attention[cite: 1541, 1669].
