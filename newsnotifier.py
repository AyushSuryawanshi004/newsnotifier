import feedparser
from win10toast import ToastNotifier
n=ToastNotifier()
f=feedparser.parse("https://zeenews.india.com/rss/world-news.xml")
for news in f['items']:
    n.show_toast(news['title'],news['summary'],duration=10)
