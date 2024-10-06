from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Refer to day 48 to 
"""
chrome_driver_path = r"C:\Users\jacky\Documents\Development\chromedriver_win32\chromedriver.exe"
"""
https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
Just put r before your normal string it converts normal string to raw string:
"""
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.amazon.com/dp/B09CTJMLQP/ref=va_live_carousel?pf_rd_r=RSRQ36WA0VYACY47JYB6&pf_rd_p=422c135c-949e-47f3-b5bb-189764debfc5&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=HighVelocityEvent&pf_rd_i=epicdeals_1_desktop&pf_rd_s=slot-4&linkCode=ilv&tag=tiffanyalliso-20&ascsubtag=Todays_Deals_211211111924&asc_contentid=amzn1.amazonlive.broadcast.5d7614f3-3746-4c86-b2eb-1e8403477ccc&pd_rd_i=B09CTJMLQP&th=1&psc=1")
price = driver.find_element(By.ID, "productTitle")
print(price.text)

"""
find element by name
find element by class name
find element by css selector, looking for an anchor tag
find element by xpath
"""
# driver.close() # close the

# driver.quit() # quit the entire program
