import urllib2
import csv
import os
import subprocess



sites = open('Sites.csv','r')

for s in sites:
	print(urllib2.urlopen(s).geturl())
	print(urllib2.urlopen(s).getcode())

