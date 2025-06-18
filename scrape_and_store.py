import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://woundreference.com/p/contents"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

base_url = "https://woundreference.com"
articles = []

for link in soup.select('a[href^="/p/"]'):
    title = link.text.strip()
    href = link.get('href')
    full_link = base_url + href
    if title and full_link not in [a[1] for a in articles]:
        articles.append((title, full_link))

conn = sqlite3.connect('knowledge_base.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS knowledge (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, url TEXT)')

cursor.executemany('INSERT INTO knowledge (title, url) VALUES (?, ?)', articles)
conn.commit()
conn.close()

print(f"✅ Scraped and saved {len(articles)} articles.")
