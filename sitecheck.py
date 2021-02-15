import urllib2
import csv
import os
import subprocess



sites = open('Sites.csv','r')

for s in sites:
	website = urllib2.urlopen(s).geturl()
	code = str(urllib2.urlopen(s).getcode())
	print('Website: ' + website + ' ---> ' + 'Code: ' + code)    

	

