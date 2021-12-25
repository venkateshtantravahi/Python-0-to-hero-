# url : http://py4e-data.dr-chuck.net/comments_1410642.xml

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# ignore ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# hitting url and retrieving data
url = input("Enter Location: ")
print("Retrieving {}".format(url))
data = urllib.request.urlopen(url, context=ctx) #nosec
data = (data.read()).decode()
print("Retrieved {} characters".format(len(data)))

# load data and count occurances
js = json.loads(data)
total, count = 0, 0
for i in js["comments"]:
    count += 1
    total += int(i["count"])
print("count: {}".format(count))
print("sum: {}".format(total))
