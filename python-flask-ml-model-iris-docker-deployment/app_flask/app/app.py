from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")
    x = np.array(features).reshape(1, -1)
    pred = model.predict(x)
    return {"prediction": int(pred[0])}
