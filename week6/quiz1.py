import urllib.request,urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
sum = 0
url = input("Enter Url - ")
js=urllib.request.urlopen(url,context=ctx).read()

info=json.loads(js)

for i in info['comments']:
    count = count+1
    sum = sum + i['count']
print("Sum : ",sum)
print("count : ",count)