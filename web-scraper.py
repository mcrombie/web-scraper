print('Using python again...hurray!')

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
# https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters

import requests
import urllib.request
import time
import csv
import io
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_cities_of_the_ancient_Near_East'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup.findAll('a')

with io.open('example.csv', "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    arr = []
    for tag in tags:
        link = tag.get('title')
        # REMOVE UNKNOWN CHARACTERS 
        print(link)
        if(link != None):
            writer.writerow([link])
            print(link)
    # time.sleep(1) #pause the code for a sec
    # writer.writerow(arr)

# with open('example.csv','rw') as fileLineCleaner:
#     for line in fileLineCleaner:
#         if not line.isspace():
#             fileLineCleaner.write(line)

print('Completed file writing!')