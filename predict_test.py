import requests

url = "http://localhost:9696/predict"
values = {
    "Age": 36,
    "SystolicBP": 120,
    "BS": 1.2,
    "BodyTemp": 37,
    "HeartRate": 102,
}

response = requests.post(url, json=values)

if response.status_code == 200:
    data = response.json()
    print(data)
    if data["High_Health_Risk"]:
        print("Must consult in an emergency.")
    else:
        print("No emergency, keep in touch.")
else:
    print("Error:", response.text)