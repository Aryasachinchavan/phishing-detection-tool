import re
import requests
import sys
from urllib.parse import urlparse

# ---------------- CHECKS ---------------- #

def check_https(url):
    return url.startswith("https")

def check_ip(url):
    domain = urlparse(url).netloc
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain)

def check_suspicious_words(url):
    suspicious = ["login", "verify", "update", "secure", "account", "bank"]
    return any(word in url.lower() for word in suspicious)

def check_length(url):
    return len(url) > 75

def check_at_symbol(url):
    return "@" in url

def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except:
        return "Error"

# ---------------- ANALYSIS ---------------- #

def analyze_url(url):
    score = 0

    https = check_https(url)
    ip = check_ip(url)
    words = check_suspicious_words(url)
    length = check_length(url)
    at_symbol = check_at_symbol(url)
    status = check_status(url)

    print("\n🔍 Analysis Result:\n")

    print("HTTPS:", "✅ Safe" if https else "❌ Not Secure")
    print("IP Address URL:", "⚠️ Suspicious" if ip else "✅ Normal")
    print("Suspicious Words:", "⚠️ Found" if words else "✅ Clean")
    print("Long URL:", "⚠️ Yes" if length else "✅ No")
    print("@ Symbol:", "⚠️ Found" if at_symbol else "✅ Not Found")
    print("Status Code:", status)

    # Risk scoring
    if not https:
        score += 2
    if ip:
        score += 3
    if words:
        score += 2
    if length:
        score += 1
    if at_symbol:
        score += 2

    print("\n🔐 Risk Score:", score)

    if score >= 6:
        verdict = "🚨 High Risk Phishing Site"
    elif score >= 3:
        verdict = "⚠️ Suspicious Site"
    else:
        verdict = "✅ Likely Safe"

    print("Result:", verdict)

    # Save report
    with open("report.txt", "w") as f:
        f.write(f"URL: {url}\n")
        f.write(f"HTTPS: {https}\n")
        f.write(f"IP: {ip}\n")
        f.write(f"Suspicious Words: {words}\n")
        f.write(f"Long URL: {length}\n")
        f.write(f"@ Symbol: {at_symbol}\n")
        f.write(f"Status Code: {status}\n")
        f.write(f"Risk Score: {score}\n")
        f.write(f"Result: {verdict}\n")

# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter URL: ")

    analyze_url(url)
