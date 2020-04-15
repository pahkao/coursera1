from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
sumoa = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    tag1 = str(tag)
    sumo = re.findall('>(\d+)<', tag1)
    print(sumo)
    sumoa += int(sumo[0])
    count += 1

print("Count is:", count)
print("Summ is:", sumoa)
