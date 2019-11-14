from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


browser = webdriver.Safari()

browser.get('https://www.exploit-db.com/')

elem = browser.find_element_by_link_text("Next")
print(elem)