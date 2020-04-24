import ssl
import json
import requests


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
response = requests.get(address)
data = json.loads(response.text)


sumo = 0
for i in data['comments']:
    sumo += i['count']

print('Sum:', sumo)