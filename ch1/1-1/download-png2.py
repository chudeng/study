import urllib.request

#assigning ULR and save route
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#download
mem = urllib.request.urlopen(url).read()

#save as file
with open(savename, mode="wb") as f:
    f.write(mem)
    print(f"{savename} of 'download-png2.py' has been saved...!")