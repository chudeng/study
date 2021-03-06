from bs4 import BeautifulSoup
html = """
<html><body>
    <ul>
        <li><a href = "http://www.naver.com">naver</a></li>
        <li><a href = "http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

# HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# find_all() 메서드로 추출하기
links = soup.find_all("a")
print(links)

# 링크 목록 출력하기
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)