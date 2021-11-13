import xml.etree.ElementTree as ET

# parsing static data
data = """<person> 
<name>John Deo</name>
<phone type="intl">
    +1 734 303 4456
</phone>
<email hide="yes" />
</person>"""

tree = ET.fromstring(data)  # making element tree
print("Name: ", tree.find("name").text)
print("Attr: ", tree.find("email").get("hide"))
