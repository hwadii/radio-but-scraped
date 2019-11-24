from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy_selenium import SeleniumRequest

user_name = "wadii"
password = "secret"

driver = webdriver.Firefox()
driver.get("https://doc.ubuntu-fr.org/liste_radio_france")
elements = driver.find_element_by_css_selector("li.node")
for element in elements:
    print(element)
driver.close()


