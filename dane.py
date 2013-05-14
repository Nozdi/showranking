import requests
import json

url = "http://127.0.0.1:8000"

data = {
    'id': '123aqwe312',
    'username': 'Vader',
    'points': 10
    }
requests.post(url, data=data)

data = {
    'id': '123aqwe312',
    'username': 'VaIer',
    'points': 20
    }
requests.post(url, data=data)

data = {
    'id': '903aqwe312',
    'username': 'Ivan',
    'points': 100
    }
requests.post(url, data=data)

data = {
    'id': '934503aq123312',
    'username': 'Delfin',
    'points': 100
    }
requests.post(url, data=data)

data = {
    'id': '934503aq123312',
    'username': 'Delfin',
    'points': 190
    }
requests.post(url, data=data)
