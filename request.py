import requests

response = requests.get('http://127.0.0.1:5000/convertir/1.0/USD/MXN')

print(response.text)
