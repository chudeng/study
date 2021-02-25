#IP check and print result thourgh API
#Read module
import urllib.request

#Read module
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
print(data)

#Transform binary to string
text = data.decode("utf-8")
print(text)