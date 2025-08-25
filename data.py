import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(f'https://opentdb.com/api.php?', params=parameters)
data = response.json()['results']


question_data = data