from sys import argv
from random import randint
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

if len(argv) < 2:
    exit(0)
target = "+".join(argv[1].split(" "))
driver = webdriver.Firefox()
driver.get(f"https://scholar.google.fr/citations?view_op=search_authors&mauthors={target}&hl=fr&oi=drw")

next_button = driver.find_element_by_css_selector("button.gs_btnPR")
previous_button = driver.find_element_by_css_selector("button.gs_btnPL")
scholars = []

while True:
    elements = driver.find_elements_by_css_selector("div.gs_ai_t")
    for element in elements:
        name = element.find_element_by_css_selector("h3.gs_ai_name").text
        email = element.find_element_by_css_selector("div.gs_ai_eml").text
        subj = element.find_element_by_css_selector("div.gs_ai_int").text
        cited = element.find_element_by_css_selector("div.gs_ai_cby").text
        entry = {"name": name, "email": email, "subj": subj, "cited": cited}
        scholars.append(entry)
    next_button.click()
    next_button = driver.find_element_by_css_selector("button.gs_btnPR")
    if not next_button.is_enabled():
        break

with open("scholars.json", "w") as f:
    json.dump(scholars, f, indent=2)

driver.close()
