
import requests

# To access your Flask application served by Waitress, 
# you should use http://localhost:8000 or http://127.0.0.1:8000 in your web browser. 
url = "http://localhost:9696/predict"  # Replace with your actual URL

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=client).json()
print(f"Does the client approve the loan?: {response['get_credit']}")
print(f"The probability that this client will get a credit is: {response['get_credit_probability']:.3f}")
