import urllib2

try:
    html = urlopen("http://pythonscrapingdontexist.com/blog")
except HTTPError as e:
    print(e)
except URLError as e:
    print("Website Can't be reached")
else:
    print("No Error")