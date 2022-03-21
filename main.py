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

max_index = 0
highscore = 0

for i in range(len(article_s)):
    if article_s[i] >= highscore:
        highscore = article_s[i]
        max_index = i
print(f"{article_t[max_index]} at {article_l[max_index]} with {article_s[max_index]} points is the winner")