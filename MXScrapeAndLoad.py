import mysql.connector
import os
import subprocess
import csv
from bs4 import BeautifulSoup
import requests


##Scrape sites for tilte, url and metadesc
sites = open('newwebsites.csv', 'w')
#urls = ['https://www.history.com']
urls = open('Sites.csv', 'r')
for url in urls:
    req = requests.get(url)
    req = req.content
    bs = BeautifulSoup(req, 'lxml')
    title = bs.title.string
    for meta in bs.find_all('meta'):
        if meta.get('name') == 'description':
            metadesc = meta.get('content')
            sites.write(title + ',' + url + ',' + metadesc + '\n')

sites.close


##Database Config
mydb = mysql.connector.connect(
  host="ec2-18-211-25-101.compute-1.amazonaws.com",
  user="bluelionmx",
  password="Idea4477&",
  database="BlueLionMX"
)

mycursor = mydb.cursor()

##Grab new sites and insert them into DB
csv_file_loc = 'newwebsites.csv'
with open(csv_file_loc, 'r') as fz:
  reader = csv.reader(fz)
  your_list = list(reader)
#filename = 'SQL'
#f = open(filename + '.txt','w')
for p in your_list:
    format_str = """INSERT INTO Sites (Title, URL, MetaDescription)
    VALUES ("{Title}", "{URL}", "{MetaDescription}");\n"""

    sql_command = format_str.format(Title=p[0], URL=p[1], MetaDescription=p[2])
    #f.write(sql_command)
    mycursor.execute(sql_command)
    mydb.commit()

#f.close()

##Insert count
rowcount = len(open(csv_file_loc).readlines())
print(rowcount)
print("Record(s) inserted")

##Close DB connection
if (mydb.is_connected()):
           mycursor.close()
           mydb.close()
           print("MySQL connection is closed")