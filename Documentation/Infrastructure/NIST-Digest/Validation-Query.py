import requests
import json

# ⚙️ Configuration - Matches your Monday VM Setup
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b" # Or your chosen 8B model

def run_validation_test():
    # This test case simulates a Wazuh alert for a failed login (AC-7)
    test_prompt = {
        "model": MODEL_NAME,
        "prompt": "Analyze this security event: 'User admin failed to login 5 times from IP 192.168.1.50'. "
                  "Map this to a NIST SP 800-53 Control and provide a Tech-Savvy Lite explanation.",
        "stream": False
    }

    print(f"🧪 Running Validation Test on {MODEL_NAME}...")
    
    try:
        response = requests.post(OLLAMA_URL, json=test_prompt)
        result = response.json()
        output = result.get('response', "")

        print("\n--- AI Response ---")
        print(output)
        print("-------------------\n")

        # Validation Logic: Check if the AI correctly identified the Control Family
        if "AC-7" in output or "Access Control" in output:
            print("✅ PASS: AI correctly mapped the event to Access Control (AC-7).")
        else:
            print("❌ FAIL: AI failed to identify the correct NIST Control.")

    except Exception as e:
        print(f"🚨 ERROR: Could not connect to the local AI engine. {e}")

if __name__ == "__main__":
    run_validation_test()
