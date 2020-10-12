import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))
total=0
for item in counts:
    number=item.text
    total=int(number)+total
print('Sum:', total)
