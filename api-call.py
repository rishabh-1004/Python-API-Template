import requests


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

data = '{ "array": [11,12,12]}'

response1 = requests.post('http://127.0.0.1:5000/api-name', headers=headers, data=data).json()
print response1