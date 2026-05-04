# 🛠️ Infrastructure Automation: NIST Ingestor & Validator

[cite_start]This folder houses the automation engine for the **LVM-Nist-Assistant**[cite: 181, 203]. [cite_start]These scripts bridge the gap between raw federal compliance data and your local AI's specialized knowledge base while maintaining a strict **No Egress Privacy Shield**[cite: 182, 183, 204].

## 📖 Overview
[cite_start]The scripts in this directory are designed to transform a general-purpose 8B Large Language Model into a specialized **NIST Compliance Assistant**[cite: 182, 205, 227]. [cite_start]By automating the "Surgical Mapping" of NIST controls, we ensure consistent, high-fidelity auditing without the risk of manual data entry errors[cite: 159, 160, 206, 228].

---

## 🐍 Core Scripts

### 1. `nist_ingestor.py`
[cite_start]The primary engine for building the AI's "NIST Brain"[cite: 184, 207, 229].
* [cite_start]**Targeted Ingestion**: Prioritizes the **Industrial Core** families: AC, AU, IR, SI, and RA to avoid overwhelming the model with 1,000+ controls[cite: 138, 185, 208, 230].
* [cite_start]**Surgical Chunking**: Implements a **1000-character chunk size** with a **200-character overlap**[cite: 24, 186, 209, 231].
* [cite_start]**Data Integrity**: Ensures critical Control IDs and specific requirements are never split or lost during the indexing process[cite: 25, 187, 210, 232].
* [cite_start]**Normalization**: Converts raw CSV data into high-fidelity text blocks for clear model context[cite: 188, 211, 233].

### 2. `validation_query.py` (Planned)
[cite_start]The "Truth-Check" script to be executed at 12:15 PM on Monday to verify system readiness[cite: 191, 212, 234].
* [cite_start]**Accuracy Verification**: Performs automated tests (e.g., "What is the requirement for AC-7?") against the ingested `nist_catalog.csv`[cite: 192, 213, 235].
* [cite_start]**Mapping Confirmation**: Validates that the AI correctly follows the **Translation Table** defined in `NIST-Logic-Base.md`[cite: 193, 214, 236].

---

## 🛡️ Security & Privacy Logic
* [cite_start]**Local-Only Processing**: All downloads, filtering, and indexing occur entirely within the isolated Ubuntu VM[cite: 189, 215, 237].
* [cite_start]**No Cloud Leakage**: Local embedding models (e.g., `nomic-embed-text`) ensure internal compliance priorities never leave your hardware[cite: 26, 70, 190, 216, 238].
* [cite_start]**Signal-to-Noise Filtering**: Automation prepares data to support **Time-Window Grouping**, preventing "Log Storms" from overwhelming the 8B model's context window[cite: 90, 195, 196, 217, 239].

---

## 🕒 Monday "Zero Hour" Instructions
1.  [cite_start]**Provision VM**: Boot your Ubuntu 24.04/26.04 environment[cite: 197, 218, 240].
2.  [cite_start]**Run Ingestor**: Execute `python3 nist_ingestor.py` to pull the catalog and build the RAG index[cite: 166, 198, 219, 241].
3.  [cite_start]**Run Validator**: Execute the validation script to confirm the "Surgical Precision" of the AI's mapping[cite: 167, 199, 220, 242].

> [!CAUTION]
> [cite_start]**Privacy Shield Reminder**: Always verify "No Egress" status by pinging an external site (e.g., `ping google.com`) before running these scripts with sensitive audit data[cite: 200, 221, 243]. [cite_start]**The ping must fail**[cite: 222, 244].
