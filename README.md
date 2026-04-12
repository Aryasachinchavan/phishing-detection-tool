🔐 Phishing Detection Tool

A Python-based phishing detection tool that analyzes URLs using multiple security checks and assigns a risk score to identify potentially malicious websites.

🚀 Features
HTTPS validation check
IP-based URL detection
Suspicious keyword scanning
URL length analysis
“@” symbol detection
HTTP status code check
Risk scoring system
Automated report generation
⚙️ How It Works

The tool analyzes a given URL using security heuristics:

Checks if HTTPS is used
Detects if the IP address is used instead of the domain
Scans for phishing-related keywords (login, verify, bank, etc.)
Measures URL length for suspicious patterns
Detects special characters like “@.”
Fetches HTTP response status

Based on these checks, a risk score is calculated.

📊 Risk Scoring System
Missing HTTPS → +2
IP-based URL → +3
Suspicious keywords → +2
Long URL → +1
“@” symbol → +2
Interpretation:
0–2 → Safe
3–5 → Suspicious
6+ → High Risk Phishing Site 🚨
🛠️ Installation
git clone https://github.com/yourusername/phishing-detection-tool.git
cd phishing-detection-tool
pip install -r requirements.txt
▶️ Usage
python3 detector.py https://example.com

OR

python3 detector.py

Then enter a URL when prompted.

📦 Requirements
requests

Install using:

pip install requests
📌 Example Output
🔍 Analysis Result:

HTTPS: ❌ Not Secure
IP Address URL: ⚠️ Suspicious
Suspicious Words: ⚠️ Found
Long URL: ⚠️ Yes
@ Symbol: ⚠️ Not Found
Status Code: 200

🔐 Risk Score: 7
Result: 🚨 High Risk Phishing Site
📁 Project Structure
phishing-detector/
│
├── detector.py
├── README.md
├── requirements.txt
└── report.txt
👨‍💻 Author

Arya Chavan

📌 Disclaimer

This tool is for educational purposes only. It is designed to help understand phishing detection techniques in cybersecurity.
