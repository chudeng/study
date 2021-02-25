#!/usr/bin/env python3

#Load libraries
import sys
import urllib.request as req
import urllib.parse as parse

#Extraction for command line variable
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

#Variable URL encoding
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

#Download
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)