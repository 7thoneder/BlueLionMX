import mysql.connector
import os
import subprocess
import csv
from bs4 import BeautifulSoup
import requests


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
  reader = csv.reader(fz, delimiter="\t")
  your_list = list(reader)
for p in your_list:
    format_str = """INSERT INTO WebSites (Title, URL, MetaDescription)
    VALUES ("{Title}", "{URL}", "{MetaDescription}");\n"""

    sql_command = format_str.format(Title=p[0], URL=p[1], MetaDescription=p[2])
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