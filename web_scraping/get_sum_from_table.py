# this file scrapes a table from the following link and gets the sum of contents in table
# link : http://py4e-data.dr-chuck.net/comments_1410640.html

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all span tags
tags = soup("span")
sum = 0
for tag in tags:
    print("TAG: ", tag)
    print("URL: ", tag.get("href", None))
    print("Contents: ", tag.contents[0])  # data in table <tr>
    sum += int(tag.contents[0])

print(sum)
