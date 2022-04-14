import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("http://opentdb.com/api.php", params=parameters)

data = response.json()
question_data = data["results"]
