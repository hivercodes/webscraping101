from bs4 import BeautifulSoup
import requests


site = requests.get("https://news.ycombinator.com/news").text

soup = BeautifulSoup(site, "html.parser")

article_t = []
article_l = []
article_s = []

article = soup.find_all(name='a', class_="titlelink")
for article_tag in article:
    article_t.append(article_tag.getText())
    article_l.append(soup.find(name='a').get("href"))

article_score = soup.find_all(name='span', class_="score")
for s in article_score:
    article_s.append(int(s.getText().strip(" points")))

max_index = max(article_s)

index_max = article_s.index(max_index)


print(f"{article_t[index_max]} at {article_l[index_max]} with {article_s[index_max]} points is the winner")