import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#Variable URL Encoding
values = {
    'stnId': '108'
}
params = urllib.parse.urlencode(values)

#Create for request URL
url = API + "?" + params
print("url=", url)

#Download
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)