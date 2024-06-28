import feedparser
import datetime

# 로컬 테스트 시 ssl 인증서 문제 해결용
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# rss 추출
feed = feedparser.parse("https://gilbert9172.tistory.com/rss")

# README 양식
markdown_text = """

### 📕 Latest Blog Posts   

"""

# 최근 블로그 추가
for i in feed['entries'][:6]:
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"
    # print(i['link'], i['title'])

# print(markdown_text)
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()