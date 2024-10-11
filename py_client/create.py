import requests


endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "clothing for Adult",
    "price": 39.99,
}

headers = {'Authorization': 'Bearer 80e520d61d1bb8b1bf1a4c454074dea3ff117b11'}
response = requests.post(endpoint, data=data, headers=headers)


print(response.json())
print(response.status_code)
