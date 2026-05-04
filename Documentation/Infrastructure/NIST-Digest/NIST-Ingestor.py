import pandas as pd
import requests
import os

# ⚙️ Configuration from Local-RAG-Config.md
CHUNK_SIZE = 1000 [cite: 1136]
CHUNK_OVERLAP = 200 [cite: 1136]
CORE_FAMILIES = ['AC', 'AU', 'IR', 'SI', 'RA'] [cite: 1251, 1275]

def download_nist_data():
    # URL for NIST SP 800-53 Rev. 5 controls (CSV format is preferred for RAG)
    # Note: On Monday, verify the latest link in your /setup/urls.md
    url = "https://csrc.nist.gov/downloads/sp800-53/rev5/sp800-53r5-control-catalog.csv"
    print("🚀 Initializing Monday 'Zero Hour' Download...")
    response = requests.get(url)
    with open("nist_catalog.csv", "wb") as f:
        f.write(response.content)
    print("✅ NIST Catalog Downloaded.")

def process_and_chunk():
    df = pd.read_csv("nist_catalog.csv")
    
    # Filter for Industrial Core families defined in NIST-Logic-Base.md [cite: 1251]
    core_df = df[df['Family'].isin(CORE_FAMILIES)]
    
    chunks = []
    for _, row in core_df.iterrows():
        # Create a "Surgical" text block for each control [cite: 1274]
        control_text = f"Control ID: {row['Control Identifier']}\n" \
                       f"Family: {row['Family']}\n" \
                       f"Requirement: {row['Control (or Control Enhancement) Name']}\n" \
                       f"Guidance: {row['Discussion']}"
        
        # Apply chunking with overlap to prevent loss of Control IDs [cite: 1137, 1276]
        for i in range(0, len(control_text), CHUNK_SIZE - CHUNK_OVERLAP):
            chunks.append(control_text[i:i + CHUNK_SIZE])
            
    print(f"📦 Created {len(chunks)} surgical chunks for the 8B model.")
    return chunks

if __name__ == "__main__":
    if not os.path.exists("nist_catalog.csv"):
        download_nist_data()
    process_and_chunk()
