# 🔐 Phishing Detection Tool

A Python-based command-line tool that analyzes URLs using a set of security heuristics and assigns a **risk score** to help identify potentially malicious or phishing websites.

---

## 🚀 Features

- HTTPS validation check
- IP-based URL detection
- Suspicious keyword scanning
- URL length analysis
- "@" symbol detection
- HTTP status code check
- Weighted risk scoring system
- Automated report generation

---

## ⚙️ How It Works

The tool evaluates a given URL against several common phishing indicators:

1. **HTTPS Check** — Verifies whether the URL uses a secure (HTTPS) connection.
2. **IP-Based URL Detection** — Flags URLs that use a raw IP address instead of a domain name.
3. **Suspicious Keyword Scan** — Searches for common phishing-related terms (e.g. `login`, `verify`, `bank`).
4. **URL Length Analysis** — Flags unusually long URLs, often used to obscure malicious links.
5. **"@" Symbol Detection** — Flags the presence of "@", which can be used to disguise the real destination of a link.
6. **HTTP Status Check** — Fetches the live HTTP response status of the target URL.

Each check contributes to a cumulative **risk score**, which determines the final classification.

---

## 📊 Risk Scoring System

| Check                | Points |
|-----------------------|--------|
| Missing HTTPS          | +2 |
| IP-based URL            | +3 |
| Suspicious keywords     | +2 |
| Long URL                 | +1 |
| "@" symbol               | +2 |

### Risk Interpretation

| Score Range | Classification |
|-------------|-----------------|
| 0 – 2  | ✅ Safe |
| 3 – 5  | ⚠️ Suspicious |
| 6+     | 🚨 High Risk Phishing Site |

---

## 🛠️ Installation

```bash
git clone https://github.com/Aryasachinchavan/phishing-detection-tool.git
cd phishing-detection-tool
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the tool by passing a URL directly as a command-line argument:

```bash
python3 detector.py https://example.com
```

Or run it without arguments and enter a URL when prompted:

```bash
python3 detector.py
```

---

## 📦 Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/)

Install the dependency manually if needed:

```bash
pip install requests
```

---

## 📌 Example Output

```
🔍 Analysis Result:

HTTPS:             ❌ Not Secure
IP Address URL:    ⚠️ Suspicious
Suspicious Words:  ⚠️ Found
Long URL:          ⚠️ Yes
@ Symbol:          ✅ Not Found
Status Code:       200

🔐 Risk Score: 7
Result: 🚨 High Risk Phishing Site
```

---

## 📁 Project Structure

```
phishing-detection-tool/
│
├── detector.py
├── README.md
├── requirements.txt
└── report.txt
```

---

## 👨‍💻 Author

**Arya Chavan**

---

## 📌 Disclaimer

This tool is intended for **educational purposes only**. It is designed to help understand the fundamentals of phishing detection techniques in cybersecurity and should not be relied upon as a sole defense mechanism against phishing attacks.
