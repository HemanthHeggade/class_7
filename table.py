from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Heggade/Desktop/Table.html")
driver.maximize_window()
driver.implicitly_wait(30)
ele = driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print(len(ele))

first_part="//*[@id='emp']/thead/tr/th["
second_part="]"
