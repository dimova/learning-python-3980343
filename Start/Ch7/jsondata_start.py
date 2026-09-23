# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# Open the URL and read the data
web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
print("Result code:", web_url.getcode())
# Read the JSON data from the source

data = web_url.read()
data = json.loads(data)


# Print the content of the 'text' field
print(data['text'])
