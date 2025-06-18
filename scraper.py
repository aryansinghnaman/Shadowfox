import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://books.toscrape.com/"


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


books = soup.find_all('h3')

# Print the book titles
print("Book Titles on the page:\n")
for book in books:
    title = book.find('a')['title']
    print("-", title)
