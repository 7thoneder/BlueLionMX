import csv
from bs4 import BeautifulSoup
import requests

#Create a file for the DB load
sites = open('newwebsites.csv', 'w')

#Opens website list and scrapes site Title, URL and MetaDescription
urls = open('Sites.txt', 'r')
websites = urls.read()
site_list = websites.split()
for url in site_list:
    req = requests.get(url)
    req = req.content
    bs = BeautifulSoup(req, 'lxml')
    title = bs.title.string
    for meta in bs.find_all('meta'):
        if meta.get('name') == 'description':
            metadesc = meta.get('content')
            #Writes site data to file that will be used for DB load
            sites.write(title + '\t' + url + '\t' + metadesc + '\n')

sites.close