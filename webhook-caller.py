import requests
import json
import random
import time

# URL of the Flask webhook receiver
webhook_url = 'http://127.0.0.1:80/webhook'

def generate_random_data():
    return {
        "event": "random_event",
        "payload": {
            "random_number": random.randint(1, 100),
            "timestamp": time.time()
        }
    }

def send_webhook():
    data = generate_random_data()
    response = requests.post(webhook_url, json=data)
    print(f"Sent: {data}")
    print("Response from webhook receiver:", response.json())

if __name__ == "__main__":
    while True:
        send_webhook()
        # Wait for a random time between 1 and 5 seconds before sending the next event
        time.sleep(random.randint(1, 5))
