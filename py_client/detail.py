import requests


endpoint = 'http://localhost:8000/api/products/1/'

response = requests.get(endpoint)
# print(response.headers)
# print(response.text)

print(response.json())
print(response.status_code)
