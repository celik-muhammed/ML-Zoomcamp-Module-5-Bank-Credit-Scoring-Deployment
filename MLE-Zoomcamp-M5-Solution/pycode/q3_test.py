
import pickle

def load(filename: str):
    # Load the object with pickle
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)
    
# Load the data preprocessing object and the trained model
dv, model = load('../model/dv.bin'), load('../model/model1.bin')

# Define the client data as a dictionary
client_data = {
    "job": "retired",
    "duration": 445,
    "poutcome": "success"
}

# Use the data preprocessing object to transform the client data
X = dv.transform([client_data])

# Make a probability prediction using the loaded model
probability = model.predict_proba(X)[:, 1]

print(f"The probability that this client will get a credit is: {probability[0]:.3f}")
