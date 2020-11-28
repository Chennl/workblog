import xml.etree.ElementTree as  ET
import os
import random
xml = os.path.join(os.getcwd(),'db','country_data.xml')
tree = ET.parse(xml)
root = tree.getroot()
#root.find()
# root.tag
# root.text
# root.items
# root.attrib
# for c in root:
#     print(c.tag,c.attrib,c.text)     
#     for cc in c:
#          print(cc.text)
# a='123333'
# if (l:=len(a)) >5:
#     print(l)

#root = ET.fromstring(country_data_as_string)
xs = [{'name':'China','rank':1,'year':2008},{'name':'USA','rank':21,'year':120}]
root = ET.Element('root')
for x in xs:
    e = ET.SubElement(root,'country')
    for k,v in x.items():
        if k=='name':
            e.set('name',str(v))
            continue
        se = ET.SubElement(e,k)
        se.text = str(v)
 
ET.dump(root)
