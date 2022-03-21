from bs4 import BeautifulSoup
import requests


site = requests.get("https://news.ycombinator.com/news").text

soup = BeautifulSoup(site, "html.parser")

article_text = soup.find(name='a', class_="titlelink").text
article_link = soup.find(name='a').get("href")
article_score = int(soup.find(name='span', class_="score").text.strip(" points"))

print(article_score)