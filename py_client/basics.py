import requests


endpoint = 'http://localhost:8000/api/create'

response = requests.post(endpoint, json={"content": "Hello World!", "title": "Greetings"})
# print(response.headers)
# print(response.text)

print(response.json())
print(response.status_code)

