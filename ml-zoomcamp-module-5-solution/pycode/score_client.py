
import requests

url = "http://127.0.0.1:8000"  # Replace with your actual URL
client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()
print(f"The probability that this client will get a credit is: {response['probability']:.3f}")
