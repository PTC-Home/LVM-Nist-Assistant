# 🛠️ Infrastructure Automation: NIST Ingestor & Validator

This folder houses the automation engine for the **LVM-Nist-Assistant**. These scripts bridge the gap between raw federal compliance data and your local AI's specialized knowledge base while maintaining a strict **No Egress Privacy Shield**.

## 📖 Overview
The scripts in this directory are designed to transform a general-purpose 8B Large Language Model into a specialized **NIST Compliance Assistant**. By automating the "Surgical Mapping" of NIST controls, we ensure consistent, high-fidelity auditing without the risk of manual data entry errors.

---

## 🐍 Core Scripts

### 1. `nist_ingestor.py`
The primary engine for building the AI's "NIST Brain".
* **Targeted Ingestion**: Prioritizes the **Industrial Core** families: AC, AU, IR, SI, and RA to avoid overwhelming the model with 1,000+ controls.
* **Surgical Chunking**: Implements a **1000-character chunk size** with a **200-character overlap** to ensure context is preserved.
* **Data Integrity**: Ensures critical Control IDs and specific requirements are never split or lost during the indexing process.
* **Normalization**: Converts raw CSV data into high-fidelity text blocks for clear model context.

### 2. `validation_query.py` (Planned)
The "Truth-Check" script to be executed at 12:15 PM on Monday to verify system readiness.
* **Accuracy Verification**: Performs automated tests against the ingested catalog to ensure the AI's "retrieval" is working.
* **Mapping Confirmation**: Validates that the AI correctly follows the Translation Table defined in your logic base.

---

## 🛡️ Security & Privacy Logic
* **Local-Only Processing**: All downloads, filtering, and indexing occur entirely within the isolated Ubuntu VM.
* **No Cloud Leakage**: Local embedding models (e.g., `nomic-embed-text`) ensure internal compliance priorities never leave your hardware.
* **Signal-to-Noise Filtering**: Automation prepares data to support **Time-Window Grouping**, preventing "Log Storms" from overwhelming the 8B model's context window.

---

## 🕒 Monday "Zero Hour" Instructions
1.  **Provision VM**: Boot your Ubuntu 24.04/26.04 environment.
2.  **Run Ingestor**: Execute `python3 nist_ingestor.py` to pull the catalog and build the RAG index.
3.  **Run Validator**: Execute the validation script to confirm the "Surgical Precision" of the AI's mapping.

> [!CAUTION]
> **Privacy Shield Reminder**: Always verify "No Egress" status by pinging an external site (e.g., `ping google.com`) before running these scripts with sensitive audit data. **The ping must fail**.
