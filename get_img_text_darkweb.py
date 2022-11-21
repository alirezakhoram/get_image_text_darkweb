import requests
import os
from bs4 import BeautifulSoup
import urllib3
import re
os.system("cls")
os.system("color a")
print("*******DarkWeb Scraper******* ")

url = str(input("\n Please Enter the onion url : "))
final_url = "http://"+str(url)+".pet"
r = requests.get(final_url)


http = urllib3.PoolManager()

#url = "https://imgur.com/"

response = http.request('GET',final_url)

soup = BeautifulSoup(response.data, 'html.parser')

images = []
text = []

for img in soup.findAll('img'):
    images.append(img.get('src'))
    
for title in soup.find_all('title') :
    text.append(title.get_text())

with open('output.txt', 'w') as file:
    file.write("Images : ")
    file.write(str(images))
    file.write("\n\n===========\n")
    file.write("\n Text : ")
    file.write(str(text))
    
print("\n images : \n")
print(images)

print("\n\n\n===========\n\n\n")
print(text)

print("****************** Alireza khoramabadi")
