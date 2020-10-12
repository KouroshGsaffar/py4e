import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read().decode()

try:
    js = json.loads(data)
except:
    js = None

total=0
counter=0

for u in js['comments']:
        total = int(u['count'])+total
        counter=counter+1
print('Count: ', counter)
print('Sum: ', total)
