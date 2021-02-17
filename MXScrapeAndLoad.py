import mysql.connector
import os
import subprocess
import csv
from bs4 import BeautifulSoup
import requests
import time

print("Scraping sites...")
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
print("Inserting records...")
time.sleep(5)

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
with open(csv_file_loc, 'r') as sites:
  reader = csv.reader(sites, delimiter="\t")
  your_list = list(reader)
for p in your_list:
    format_str = """INSERT INTO WebSites (Title, URL, MetaDescription)
    VALUES ("{Title}", "{URL}", "{MetaDescription}");\n"""

    sql_command = format_str.format(Title=p[0], URL=p[1], MetaDescription=p[2])
    mycursor.execute(sql_command)
    mydb.commit()


##Insert count
rowcount = str(len(open(csv_file_loc).readlines()))
print(rowcount + " Record(s) inserted")
#print("Record(s) inserted")

##Close DB connection
if (mydb.is_connected()):
           mycursor.close()
           mydb.close()
           print("MySQL connection is closed")

print("DONE")