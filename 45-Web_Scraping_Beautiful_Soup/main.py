
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(f"Title: {soup.title.text}")
'''first occurence'''
# first_tag = soup.find(name="a", class_="storylink")
# article_text = first_tag.text
# article_link = first_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)
'''list of data'''
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

'''article with max upvotes'''
max_upvotes = max(article_upvotes)
print(f"max_upvotes: {max_upvotes}")
index_of_max = article_upvotes.index(max_upvotes)
print(f"index of max: {index_of_max}")
print(f"Title: {article_texts[index_of_max+1]}") #+1 due to new entry entering list with no upvotes yet*
print(f"Link: {article_links[index_of_max+1]}")
print(f"Upvotes: {article_upvotes[index_of_max]}")

'''------------------------------------------------------------------------------'''

'''Using website.html'''
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")

'''print entire html'''
# print(soup)

'''print html with indents using prettify'''
# print(soup.prettify())

'''navigate data structure: https://www.crummy.com/software/BeautifulSoup/bs4/doc/'''
# print(f"title: {soup.title}")
# print(f"title.string: {soup.title.string}")
# '''First Anchor tags'''
# print(f"first anchor tag: {soup.a}")
# print(f"first anchor tag: {soup.a.string}")
# '''First paragraph tag'''
# print(f"first paragraph: {soup.p}")

'''find_all, return list of anchor tags'''
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     '''text of anchor tags'''
#     # print(tag.getText())
#     '''links of anchor tags'''
#     print(tag.get("href"))

'''finding specific id or class on html site'''
# heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.text)
# print(heading.getText())
# print(heading.name)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.text)

# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)

'''list of specifics'''
# headings = soup.select(".heading")
# print(headings)