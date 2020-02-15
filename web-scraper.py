print('Using python again...hurray!')

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_cities_of_the_ancient_Near_East'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup.findAll('a')

# link = one_a_tag['href']


arr = []
for tag in tags:
    link = tag.get('title')
    if(link != None):
        print(tag.get_text())
    # print('/n')
    # arr.append(tag)
    # time.sleep(1) #pause the code for a sec


 

# print(arr)