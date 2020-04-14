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
l = list()

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    tag1 = str(tag)
    sumo = re.findall('>(\d+)<', tag1)
    l.append(sumo)
    count += 1

sumoa = 0
for i in l:
    for y in i:
        sumoa += int(y)

print("Count is:", count)
print("Summ is:", sumoa)


# need suggestion how to make it easier
# help please, my email: olkhovskiy91@gmail.com
# thank you :)