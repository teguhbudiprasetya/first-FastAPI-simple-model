import requests

data = {
    "number":5
}


API_KEY = "http://127.0.0.1:8000/prediction/"


predict = requests.post(url = API_KEY, json=data)

print(predict.json())
