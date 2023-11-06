import requests


url = 'http://localhost:9696/predict'

pregnancy_id = 'xyz-123'
values = {
    "Age": 36,
    "SystolicBP": 18,
    "BS": 1.2,
    "HeartRate": 102


response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)