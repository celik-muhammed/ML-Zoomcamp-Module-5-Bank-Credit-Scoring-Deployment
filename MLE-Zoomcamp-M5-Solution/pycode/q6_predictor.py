
from flask import Flask, request, jsonify
import pickle


def load(filename: str):
    # Load the object with pickle
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

# Load the data preprocessing object and the trained model
dv, model = load('dv.bin'), load('model2.bin')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # client = request.get_json()
    client = request.json

    # Use the data preprocessing object to transform the input data
    X = dv.transform([client])

    # Make a probability prediction using the loaded model
    probability = model.predict_proba(X)[:, 1]

    result = {
        'get_credit_probability': float(probability),
        'get_credit': bool(probability >= 0.5)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696, use_reloader=False)
