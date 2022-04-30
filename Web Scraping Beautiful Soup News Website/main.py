from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text


# print(response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
# article_tag = soup.find(name="a", class_="titlelink")
# print(article_tag.getText())   #This printed the article name.

#this is to find the first occurence in the web page
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

#to find a list of all the stuff on web page.
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

#for the challenge, going to get the list and sort by which article has most points.
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
# print(article_texts[largest_index])
# print(article_links[largest_index])
# print(article_upvotes[largest_index])

print(article_texts)
# print(article_texts[0]) if I want to get the first item in the list.
print(article_links)
print(article_upvotes)