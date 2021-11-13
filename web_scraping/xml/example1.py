import xml.etree.ElementTree as ET
# static input in string form
input = '''<stuff> 
    <users>
        <user x="2">
            <id>001</id>
            <name>John</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input) # forming elemens-tree from string
lst = stuff.findall('users/user') # getting users->user tag in tree
print('User count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))