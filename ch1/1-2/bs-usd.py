from bs4 import BeautifulSoup
import urllib.request

# HTML 가져오기
url = "https://finance.daum.net/quotes/A219750?period=day#home"
res = urllib.request.urlopen(url)

# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출하기
price = soup.select_one("#boxSummary > div > span > span > span").string
print("지티지웰니스 =", price)