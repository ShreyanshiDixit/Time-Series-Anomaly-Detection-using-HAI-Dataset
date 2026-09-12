import requests

# ===========================
# CONFIG
# ===========================
BASE_URL = "http://127.0.0.1:8000"
API_KEY  = "Team_Dimonds2026_xyzdaiict"
CSV_PATH = "D:/backend/backend/small.csv"  # ← change this to your actual CSV file path

HEADERS = {"x-api-key": API_KEY}

# ===========================
# STEP 1: UPLOAD CSV
# ===========================
print("Uploading CSV...")
with open(CSV_PATH, "rb") as f:
    res = requests.post(f"{BASE_URL}/upload", headers=HEADERS, files={"file": f})

print(f"Status: {res.status_code}")
print(f"Response: {res.json()}")
print()

# ===========================
# STEP 2: GET ANOMALIES
# ===========================
print("Fetching anomalies...")
res = requests.get(f"{BASE_URL}/anomalies", headers=HEADERS)
anomalies = res.json()
print(f"Total anomalies: {len(anomalies)}")

if anomalies:
    print(f"First anomaly: {anomalies[0]}")
    print()

    # ===========================
    # STEP 3: GET ADVISORY
    # ===========================
    first_idx = anomalies[0]["window_idx"]
    print(f"Getting advisory for window_idx={first_idx}...")
    res = requests.post(
        f"{BASE_URL}/explain",
        headers={**HEADERS, "Content-Type": "application/json"},
        json={"window_idx": first_idx}
    )
    print(f"Advisory: {res.json()['advisory']}")
else:
    print("No anomalies found.")