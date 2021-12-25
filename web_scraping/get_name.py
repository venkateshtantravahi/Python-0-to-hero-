# start at : http://py4e-data.dr-chuck.net/known_by_Caitlyn.html
"""
Find the link at position 18. Follow that link. Repeat this process 7 times. The answer is the 
last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: M
"""

import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

# creating secure socket layer before hitting url
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# user input
url = input("Enter URL - ")
repeat = int(input("Enter the number of repetitions: "))
position = int(input("Enter the link position: "))


for i in range(repeat):
    # if url.lower().startswith("http"):
    #     req = urllib.request.Request(url)
    # else:
    #     raise ValueError from None
    # with urllib.request.urlopen(req) as response:
    #     html = response.read()  # nosec
    html = urllib.request.urlopen(url, context=ctx).read()  # nosec
    soup = BeautifulSoup(html, "html.parser")  # parsing html using bs4
    tags = soup("a")  # retrieving anchor objects
    count = 0
    for tag in tags:
        count += 1

        if count > position:
            break
        url = tag.get("href", None)
        name = tag.content[0]

print(name)
