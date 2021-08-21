import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter the url: ")
sum = 0

data = urllib.request.urlopen(url, context=ctx).read()

# print('Retrieved', len(data), 'characters')
# print(data.decode())

tree = ET.fromstring(data)
lst=tree.findall('comments/comment')
for i in lst:
    sum +=int(i.find('count').text)
print(sum)