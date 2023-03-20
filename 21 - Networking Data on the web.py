#xml y json: representing data on the web
import xml.etree.ElementTree as ET

data = ''' <person>
        <name> Nur </name>
        <phone type= "intl">
          12345 
        </phone>
        <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:"), tree.find("email").get("hide")

#json

import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])





