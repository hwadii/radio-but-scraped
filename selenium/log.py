import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from scrapy_selenium import SeleniumRequest

driver = webdriver.Firefox()
driver.get("https://doc.ubuntu-fr.org/liste_radio_france")
elements = driver.find_elements_by_css_selector("li.node")
result = []

for element in elements:
    title = element.find_element_by_css_selector("div.li > a.urlextern")
    title = title.text
    try:
        url = element.find_element_by_css_selector(
            "ul.fix-media-list-overlap > li.level2 > div.li > a.urlextern")
        url = url.get_attribute("href")
    except:
        url = ""
    item = {"title": title, "url": url}
    result.append(item)

driver.close()

with open("radios.json", "w") as f:
    json.dump(result, f, indent=2, sort_keys=True)
