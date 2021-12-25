import urllib.request, urllib.parse, urllib.error
import json, ssl

service_url = "http://py4e-data.dr-chuck.net/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parms = dict()
    parms["address"] = address
    parms["key"] = 42
    url = service_url + urllib.parse.urlencode(parms)
    print("Retrieving url", url)
    uh = urllib.request.urlopen(url, context=ctx) #nosec
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("====== Failure To Retrieve ======")
        print(data)
        continue

    # print(data)
    place_id = js["results"][0]["place_id"]
    print("Place id ", place_id)
