from bs4 import BeautifulSoup
import requests

link = input("input an URL to retrive link:")


if("https" or "http") in link:
    stream = requests.get(link)
else:
    stream = requests.get("https://"+link)

soup = BeautifulSoup(stream,"html.parser")
links= []
for link in soup.find_all("a"):
    links.append(link.get("href"))
soup.find_all
     

rint(stream.text)