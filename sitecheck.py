import urllib2
import csv
import os
import subprocess



sites = open('Sites.txt','r')

for s in sites:
	website = urllib2.urlopen(s).url
	code = str(urllib2.urlopen(s).code)
	print('Website: ' + website + ' ---> ' + 'Code: ' + code)

	

