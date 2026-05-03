from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# load model
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")  

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = list(data.values())
    features = np.array(features).reshape(1, -1)

    features = scaler.transform(features)

    pred = model.predict(features)[0]

    if pred == 1:
        result = "Benign"
    else:
        result = "Malignant"

    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True) 