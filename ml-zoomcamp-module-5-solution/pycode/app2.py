
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the data preprocessing object and the trained model
with open('dv.bin', 'rb') as dv_file, open('model2.bin', 'rb') as model_file:
    dv = pickle.load(dv_file)
    model = pickle.load(model_file)

@app.route('/', methods=['POST'])
def predict():
    data = request.json

    # Use the data preprocessing object to transform the input data
    X = dv.transform([data])

    # Make a probability prediction using the loaded model
    probability = model.predict_proba(X)[:, 1]

    return jsonify({'probability': probability[0]})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
