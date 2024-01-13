import sqlite3
import sys

def insert_url(site_name, url):
    conn = sqlite3.connect('data/articles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Insert an url
    cursor.execute('INSERT INTO url_list (site_name, url) VALUES (?, ?)', (site_name, url))
    conn.close()

def insert_article(title, author, publish_date, content, url_id):
    conn = sqlite3.connect('data/articles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Insert an url
    cursor.execute('INSERT INTO articles (title, author, publish_date, content, url_id) VALUES (?, ?, ?, ?, ?)', 
                   (title, author, publish_date, content, url_id))
    
    conn.close()

# Check if the correct number of command-line arguments is provided
if len(sys.argv) == 3:
    # Extract site_name and url from command-line arguments
    site_name = sys.argv[1]
    url = sys.argv[2]

    # Call the insert_url function with the provided arguments
    insert_url(site_name, url)

    



