# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#
import xml.dom.minidom as minidom

# use the parse() function to load and parse an XML file
doc = minidom.parse("samplexml.xml")


# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)


# get a list of XML tags from the document and print each one
tags = doc.getElementsByTagName("skill")
for tag in tags:
    print(tag.getAttribute("name"))

    
# create a new XML tag and add it into the document
new_tag = doc.createElement("skill")
new_tag.setAttribute("name", "jQuery")
doc.firstChild.appendChild(new_tag)

for tag in doc.getElementsByTagName("skill"):
    print(tag.getAttribute("name"))