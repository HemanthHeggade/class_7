import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://phptravels.com/")
browser.maximize_window()
browser.implicitly_wait(30)
browser.delete_all_cookies()