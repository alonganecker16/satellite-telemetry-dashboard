import time
import random
import requests
import uuid

API_URL = "INSERT API GATEWAY URL HERE!!!!!!!!!"
SATELLITE_ID = f"SAT-{str(uuid.uuid4())[:8]}"

# Generate random data that the satellite will transmit between specific ranges
def generate_satellite_data():
    return {
        "satellite_id": SATELLITE_ID,
        "timestamp": int(time.time()),
        "position": {
            "lat": random.uniform(-90, 90),
            "lon": random.uniform(-180,180),
            "alt": random.uniform(400, 600)
        },
        "velocity": round(random.uniform(7.5, 8.2), 2),
        "temp": random.randint(60, 90),
        "battery": random.randint(50, 100),
        "signal_strength": random.randint(80, 100)
    }

# Make it a 10% chance that there is anomalic data so we can track inconsistencies in the data
def inject_anomalies(data):
    if random.random() < 0.1:
        print("ANOMALY ADDED!!!!!!!!!!!!!!!!")
        anomaly_type = random.choice(["temp", "battery", "signal"])

        if anomaly_type == "temp":
            data["temp"] = random.randint(120, 180)
        elif anomaly_type == "battery":
            data["battery"] = random.randint(5, 15)
        elif anomaly_type == "signal":
            data["signal_strength"] = random.randint(0, 30)
        
    return data

# Send the data to the API so it can be published and then visualized via the dashboard
def send_data():
    data = generate_satellite_data()
    data = inject_anomalies(data)

    print(f"Sent: {data} | Status: 400")

    # try:
    #     response = requests.post(API_URL, json=data, timeout=2)
    #     print(f"Sent: {data} | Status: {response.status_code}")
    # except Exception as e:
    #     print(f"Error sending data: {e}")

# Start here, sending data to the API every second
if __name__ == "__main__":
    print(f"Starting data simulation for {SATELLITE_ID}")
    while True:
        send_data()
        time.sleep(1)