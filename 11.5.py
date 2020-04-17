import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


list_of_digits = []
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
data_decode = data.decode()
print('Retrieved ' + str(len(data_decode)) + ' characters')
tree = ET.fromstring(data)
count = tree.findall('.//count')  # find all elements w/ <count>

for i in range(len(count)):  # append all digits in elements to list
    counts = ET.tostring(count[i])
    digits = re.findall('\d+', str(counts))
    list_of_digits.append(digits)


sumo = 0
for i in list_of_digits:  # summ all values in list
    for y in i:
        sumo += int(y)

print('Count:', len(count))
print('Sum:', sumo)