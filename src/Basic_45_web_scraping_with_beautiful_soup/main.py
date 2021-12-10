from bs4 import BeautifulSoup
# beautiful soup 4 for web scraping
#import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# html.parser or lxml may not work in some websites

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
"""
Find the info that we look for using Beautiful Soup
"""

