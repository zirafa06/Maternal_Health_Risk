import pickle
import sklearn
from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.pkl'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('HealthRisk')

@app.route('/predict', methods=['POST'])
def predict():
    values = request.get_json()

    X = ([values])
    y_pred = model.predict(X)

    result = {
        'Hight_Health_Risk': y_pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)