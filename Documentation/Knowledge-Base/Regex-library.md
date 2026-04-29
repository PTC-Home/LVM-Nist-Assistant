# NIST Regex Library: Surgical Log Filtering

## 🛡️ Purpose
[cite_start]This library provides standardized Regular Expression (Regex) patterns to sift through massive log files[cite: 25, 33]. [cite_start]These patterns extract relevant evidence for NIST auditing while maintaining our **Privacy Shield** by redacting sensitive information before AI analysis[cite: 27, 33].

---

## 🔍 NIST Violation Patterns
[cite_start]Use these patterns to identify technical evidence that maps directly to NIST SP 800-53 or CSF controls[cite: 33, 44].

| Violation Category | Regex Pattern (Example) | NIST Control ID |
| :--- | :--- | :--- |
| **Failed Access Attempts** | `(?i)failed|failure|invalid user` | [cite_start]**AC-2** (Account Management) [cite: 35, 165] |
| **Unauthorized IPs** | `^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$` | [cite_start]**AC-4** (Info Flow Enforcement) [cite: 26, 149]|
| **Outdated Encryption** | `(?i)TLSv1\.[01]` | [cite_start]**SC-8** (Transmission Confidentiality) [cite: 28, 152] |
| **System Anomalies** | `(?i)critical|alert|emergency` | [cite_start]**AU-6** (Audit Record Review) [cite: 42, 172] |

---

## 🔐 Privacy & Masking Patterns
[cite_start]To uphold our **Privacy Shield**, use these patterns to redact Personally Identifiable Information (PII) before the data leaves this local environment[cite: 27, 260].

> [!WARNING]
> [cite_start]**Universal Compliance Requirement:** PII must be redacted in all automated summaries to prevent data leakage, even within a local VM[cite: 27, 58].

* [cite_start]**Social Security Numbers:** `\b\d{3}-\d{2}-\d{4}\b` [cite: 27]
* [cite_start]**Credit Card Formats:** `\b(?:\d{4}[ -]?){3}\d{4}\b` [cite: 27]
* [cite_start]**Internal Email Domains:** `[a-zA-Z0-9._%+-]+@company\.local` [cite: 27]

---

## 🛠️ Tooling & Integration
[cite_start]These patterns are designed for use with local utilities to ensure zero internet egress[cite: 32, 58]:
* [cite_start]**`grep -E`**: For rapid command-line log filtering[cite: 32].
* [cite_start]**`python re`**: For complex pre-processing scripts in the `/infrastructure` folder[cite: 32, 53].
* [cite_start]**Wazuh Decoders**: Integrated into your Wazuh rules to trigger AI summarization[cite: 34, 42].

---

> [!TIP]
> [cite_start]**Security Outcome:** Using Regex to clean raw Wazuh logs removes noise and ensures the AI only processes "high-fidelity" signals, improving the accuracy of your "Tech-Savvy Lite" reports[cite: 46, 257].
