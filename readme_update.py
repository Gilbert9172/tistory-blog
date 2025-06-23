import feedparser
import ssl
from datetime import datetime


def to_iso8601(dt: datetime) -> str:
    raw = dt.strftime("%Y-%m-%d %H:%M:%S%z")
    return raw[:-2] + ":" + raw[-2:]


# To ignore ssl certification on local env
ssl._create_default_https_context = ssl._create_unverified_context

# Extract feed from rss
blogUrl: str = "https://gilbert9172.tistory.com/rss"
feed = feedparser.parse(blogUrl)

# Extract prev publishing datetime from README.md
try:
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_content = file.read()
except FileNotFoundError:
    print("Error: README.md not found in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")

# Convert each str to datetime
latestPublishedDate: datetime = datetime.strptime(
    feed['feed']['published'], "%a, %d %b %Y %H:%M:%S %z"
)
prevPublishedDate: datetime = datetime.fromisoformat(readme_content)

markdown_source = latestPublishedDate if latestPublishedDate > prevPublishedDate else prevPublishedDate

f = open("README.md", mode="w", encoding="utf-8")
f.write(to_iso8601(markdown_source))
f.close()
