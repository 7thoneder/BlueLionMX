import mysql.connector
import os
import subprocess
import csv

mydb = mysql.connector.connect(
  host="ec2-18-211-25-101.compute-1.amazonaws.com",
  user="bluelionmx",
  password="Idea4477&",
  database="BlueLionMX"
)

mycursor = mydb.cursor()

csv_file_loc = 'websites.csv'
with open(csv_file_loc, 'r') as fz:
  reader = csv.reader(fz)
  your_list = list(reader)
filename = 'SQL'
f = open(filename + '.sql','w')
for p in your_list:
    format_str = """INSERT INTO Sites (Title, URL, MetaDescription)
    VALUES ("{Title}", "{URL}", "{MetaDescription}");\n"""

    sql_command = format_str.format(Title=p[0], URL=p[1], MetaDescription=p[2])
    f.write(sql_command)

f.close()

#sql_file = open('SQL.csv', 'r')
#new_sql_file = f.open()
  
#for sqlcommand in sql_file:
#    mycursor.execute(sqlcommand)
#mydb.commit()


#print(mycursor.rowcount, "record inserted.")

#if (mydb.is_connected()):
#           mycursor.close()
#            mydb.close()
#           print("MySQL connection is closed")