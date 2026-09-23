# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
import urllib.request

url = "http://www.example.com"
response = urllib.request.urlopen(url)
data = response.read()
print(data)