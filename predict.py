import pickle

import numpy as np
from flask import Flask, jsonify, request

model_file = "model.pkl"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = request.get_json()
        X = np.array(
            [
                [
                    values["Age"],
                    values["SystolicBP"],
                    values["BS"],
                    values["HeartRate"],
                    values["BodyTemp"],
                ]
            ]
        )
        y_pred = model.predict(X)
        result = {
            "High_Health_Risk": bool(y_pred[0])
        }  # Convert the numpy boolean to Python native boolean

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)