import requests


endpoint = 'http://localhost:8000/api/products/133243/'

response = requests.get(endpoint)

print(response.json())
print(response.status_code)
