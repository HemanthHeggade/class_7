import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(30)

element=driver.find_element_by_xpath("//span[contains(text(),'men')]")
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

