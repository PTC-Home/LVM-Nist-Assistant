import requests
import json
import sys

# --- CONFIGURATION ---
# Desktop side (Wazuh Manager)
WAZUH_MANAGER_IP = "100.x.x.x"  # Replace with Desktop Tailscale IP
WAZUH_API_PORT = "55000"
WAZUH_USER = "admin"
WAZUH_PASS = "SecretPassword123"

# Laptop side (Local AI)
AI_LOCAL_HOST = "localhost"
AI_PORT = "11434"
MODEL_NAME = "llama3.3:8b-instruct-q8_0" # Recommended precision

# --- STEP 1: AUTHENTICATION ---
def get_wazuh_token():
    """Authenticates with the Wazuh API and returns a JWT token."""
    auth_url = f"https://{WAZUH_MANAGER_IP}:{WAZUH_API_PORT}/security/user/authenticate"
    try:
        response = requests.get(auth_url, auth=(WAZUH_USER, WAZUH_PASS), verify=False)
        if response.status_code == 200:
            return response.json().get('data', {}).get('token')
        return None
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

# --- STEP 2: LOG EXTRACTION ---
def get_security_alerts(token, min_level=12):
    """Fetches high-level security alerts for NIST analysis."""
    alerts_url = f"https://{WAZUH_MANAGER_IP}:{WAZUH_API_PORT}/alerts"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'level': f'{min_level}+', 'limit': 5} # Surgical filtering
    
    response = requests.get(alerts_url, headers=headers, params=params, verify=False)
    return response.json().get('data', {}).get('affected_items', [])

# --- STEP 3: AI ANALYSIS ---
def analyze_alert_with_ai(alert):
    """Feeds the alert to the Auditor Persona for Tech-Savvy Lite reporting."""
    ai_url = f"http://{AI_LOCAL_HOST}:{AI_PORT}/api/generate"
    
    # Custom prompt leveraging our Auditor Persona rules
    prompt = (
        f"Analyze this security alert: {json.dumps(alert)}\n\n"
        "Instructions:\n"
        "1. Map this to a NIST SP 800-53 or CSF control.\n"
        "2. Provide a 'Tech-Savvy Lite' business risk summary.\n"
        "3. Use GitHub-style [!CAUTION] or [!WARNING] flags."
    )

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(ai_url, json=payload)
    return response.json().get('response')

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    token = get_wazuh_token()
    if not token:
        sys.exit("Failed to connect to Wazuh Manager.")

    alerts = get_security_alerts(token)
    for alert in alerts:
        report = analyze_alert_with_ai(alert)
        print("-" * 30)
        print(report)
