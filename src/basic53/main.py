from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import time

GOOGLE_FORM_URL = "https://forms.gle/VMhtUu36gKYUD6ct8"
CHROME_DRIVER_PATH = r"C:\Users\jacky\Documents\Development\chromedriver_win32\chromedriver.exe"
ZILLOW_URL = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-84.44937810656634%2C%22east%22%3A-84.04769048449603%2C%22south%22%3A39.464113115956756%2C%22north%22%3A39.67636082407137%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8"
}

response = requests.get(ZILLOW_URL, headers=header)
# print(response) # Debug
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all(name='a', class_="list-card-link list-card-link-top-margin")
price_list = soup.find_all(name='div', class_='list-card-price')
# print(links) # Debug

addresses = []
hyper_link = []
price = [float(priceIndex.getText().split('$')[1].replace(',', '')) for priceIndex in price_list]

for link in links:
    addresses.append(link.getText())
    hyper_link.append(link.get("href"))

print(hyper_link)

if len(addresses) == len(hyper_link) == len(price):
    # initial robotic driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    for i in range(len(addresses)):
        driver.get(GOOGLE_FORM_URL)
        time.sleep(0.5)
        autofill = driver.find_element(By.XPATH, '//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
        autofill.send_keys(addresses[i], Keys.TAB, price[i], Keys.TAB, hyper_link[i], Keys.TAB, Keys.ENTER)
        print(i)
        time.sleep(2)
    driver.quit()
