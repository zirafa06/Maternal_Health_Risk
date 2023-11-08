import requests


url = 'http://localhost:9696/predict'


values = {
    "Age": 36,
    "SystolicBP": 18,
    "BS": 1.2,
    "HeartRate": 102


response = requests.post(url, json=values).json()
print(response)

if response['Hight_Health_Risk'] == True:
    print('must consult in emergency')
else:
    print('no emergency, keep in touch')