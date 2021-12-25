import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read() #nosec
soup = BeautifulSoup(html, "html.parser")

# retrieve all anchor tags
tags = soup("a")
for tag in tags:
    print("TAG: ", tag)
    print("URL: ", tag.get("href", None))
    print("Contents: ", tag.contents[0])
    print("Attr:", tags.attrs)
