from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

GOOGLE_FORM_URL = "https://forms.gle/VMhtUu36gKYUD6ct8"
CHROME_DRIVER_PATH = r"C:\Users\jacky\Documents\Development\chromedriver_win32\chromedriver.exe"
ZILLOW_URL = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-88.307021484375%2C%22east%22%3A-81.88001953125%2C%22south%22%3A39.474418864543466%2C%22north%22%3A42.79142047971363%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A300000%2C%22max%22%3A800000%7D%2C%22mp%22%3A%7B%22min%22%3A1003%2C%22max%22%3A2674%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8"
}

response = requests.get(ZILLOW_URL, headers=header)
print(response)
soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify())
