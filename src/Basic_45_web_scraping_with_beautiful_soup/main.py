from bs4 import BeautifulSoup
# beautiful soup 4 for web scraping
# import lxml

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# html.parser or lxml may not work in some websites

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
"""
Find the info that we look for using Beautiful Soup
"""

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#     # print(tag.getText())

# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

import requests

response = requests.get("")

