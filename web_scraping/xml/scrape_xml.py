# url : http://py4e-data.dr-chuck.net/comments_1410642.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 
import ssl

# ignore secure socket layer
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# hitting url 
url = input('Enter URL - ')
data = urllib.request.urlopen(url, context=ctx)
data = (data.read()).decode()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
sum = 0
for item in lst:
  sum += int(item.find('count').text)

print(sum)