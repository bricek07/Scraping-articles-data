import sqlite3

conn = sqlite3.connect('data/articles.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the URL table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS url_list (
        id INTEGER PRIMARY KEY,
        site_name TEXT, 
        url TEXT NOT NULL
    )
''')

# Create the Articles table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        publish_date TEXT,
        content TEXT,
        url_id INTEGER,
        FOREIGN KEY (url_id) REFERENCES url_list (id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
