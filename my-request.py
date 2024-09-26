import requests

url = "http://127.0.0.1:8000/todo/"

data = {
    "id": 1,
    "item"  :"Cook a dinner."

}

response = requests.post(url,json=data)


print(f"Status_code = {response.status_code}")

print(f"Response = {response.json()}")
