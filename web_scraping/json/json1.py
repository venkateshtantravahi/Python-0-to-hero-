import json

data = """{
    "name": "Chuck",
    "phone":{
        "type":"intl",
        "number": "+1 734 303 568"
    },
    "emial": {
        "hide": "yes"
    }
}"""

# we can also write our data in the following way also :
"""
data = [
    {
        "id": "001",
        "x" : "2",
        "name": "venkat"
    } ,
    {
        "id" : "009",
        "x" :"7",
        "name" : "john"
    }
]"""

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])
