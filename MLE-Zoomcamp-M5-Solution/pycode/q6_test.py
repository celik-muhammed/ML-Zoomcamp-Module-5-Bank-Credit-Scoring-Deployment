
import requests

url = "http://localhost:9696/predict"  # Replace with your actual URL
client = {"job": "retired", "duration": 445, "poutcome": "success"}

response = requests.post(url, json=client).json()
print(f"Does the client approve the loan?: {response['get_credit']}")
print(f"The probability that this client will get a credit is: {response['get_credit_probability']:.3f}")
