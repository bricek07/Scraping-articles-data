import requests
from bs4 import BeautifulSoup 
import feedparser
import newspaper

airbnb_blog_url = 'https://medium.com/airbnb-engineering/data/home'
google_feed_url = 'http://feeds.feedburner.com/blogspot/gJZg'

def scrape_news_from_feed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        # create a newspaper article object
        article = newspaper.Article(entry.link)
        # download and parse the article
        article.download()
        article.parse()
        # extract relevant information
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })

    return articles

print(scrape_news_from_feed(google_feed_url)[0]['content'])

