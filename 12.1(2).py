import ssl
import json
import urllib.request, urllib.parse, urllib.error


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
response = urllib.request.urlopen(address, context=ctx)
data = response.read()
info = json.loads(data)


sumo = 0
for i in info['comments']:
    sumo += i['count']

print('Sum:', sumo)