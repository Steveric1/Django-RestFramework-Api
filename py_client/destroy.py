import requests


endpoint = 'http://localhost:8000/api/products/2/update/'

data = {
    "title": "Chicken is amazing"
}

response = requests.put(endpoint, data=data)
# print(response.headers)
# print(response.text)

print(response.json())
print(response.status_code)
