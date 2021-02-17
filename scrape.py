import csv
from bs4 import BeautifulSoup
import requests


sites = open('newwebsites.csv', 'w')
urls = open('Sites.txt', 'r')
websites = urls.read()
site_list = websites.split()
#urls = ['https://www.nhl.com','https://www.history.com','https://www.cnbc.com']
for url in site_list:
    req = requests.get(url)
    req = req.content
    bs = BeautifulSoup(req, 'lxml')
    title = bs.title.string
    for meta in bs.find_all('meta'):
        if meta.get('name') == 'description':
            metadesc = meta.get('content')
            sites.write(title + '\t' + url + '\t' + metadesc + '\n')

sites.close