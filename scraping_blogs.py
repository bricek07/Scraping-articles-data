import feedparser
import newspaper
import sqlite3
import insert_db

airbnb_blog_url = 'https://medium.com/airbnb-engineering/data/home'
google_feed_url = 'http://feeds.feedburner.com/blogspot/gJZg'
medium_tag_list = ['data-science', 'python', 'machine-learning']
medium_feed_urls = ['https://medium.com/feed/tag/' + s for s in medium_tag_list]

def retrieve_urls(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute('SELECT url FROM url_list')
    urls = cursor.fetchall()
    conn.close()

    return urls

def retrieve_max_date(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute('SELECT MAX(DATE(publish_date)) FROM articles')

    # Fetch the result
    max_date = cursor.fetchone()[0]

    # Print the maximum date
    print("Max Date:", max_date)

    conn.close()


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
            'title': entry.title,
            'author': entry.author_detail.name,
            'publish_date': entry.published,
            'content': entry.content
        })

    return articles

max_date = retrieve_max_date(r'/data/articles.db')
print(max_date)

# articles = scrape_news_from_feed(google_feed_url)
# for article in articles:
#     print(article['content'])
#     break

# urls_list = [airbnb_blog_url, google_feed_url]
# for url in medium_feed_urls:
#     urls_list.append(url)

# print(urls_list)

# for url in urls_list:
#     print(url)
#     articles = scrape_news_from_feed(url)

#     for article in articles:
#         with open('articles.txt', 'a') as file:
#             file.write(article['content'])


