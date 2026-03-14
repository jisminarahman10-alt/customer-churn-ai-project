from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open('../model/churn_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Customer Churn Prediction API is Running"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    features = [[
        data["CreditScore"],
        data["Age"],
        data["Tenure"],
        data["Balance"],
        data["NumOfProducts"],
        data["HasCrCard"],
        data["IsActiveMember"],
        data["EstimatedSalary"],
        data["Geography_France"],
        data["Geography_Germany"],
        data["Geography_Spain"],
        data["Gender_Female"],
        data["Gender_Male"],
        data["Exited"]
    ]]

    prediction = model.predict(features)

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)