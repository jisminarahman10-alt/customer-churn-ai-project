import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "CreditScore":650,
    "Age":35,
    "Tenure":5,
    "Balance":50000,
    "NumOfProducts":2,
    "HasCrCard":1,
    "IsActiveMember":1,
    "EstimatedSalary":60000,
    "Geography_France":0,
    "Geography_Germany":1,
    "Geography_Spain":0,
    "Gender_Female":0,
    "Gender_Male":1,
    "Exited":0
}

response = requests.post(url, json=data)

print("Response from API:")
print(response.text)