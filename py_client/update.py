import requests


endpoint = 'http://localhost:8000/api/products/2/update/'

data = {
    "title": "Chicken is updated",
    "content": "I change this content",
    "price": 82.99
}

response = requests.put(endpoint, data=data)
# print(response.headers)
# print(response.text)

print(response.json())
print(response.status_code)
