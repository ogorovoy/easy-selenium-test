from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element_by_link_text("Dropdown").click()
time.sleep(2)

select = Select(driver.find_element_by_id('dropdown'))
time.sleep(2)

select.select_by_value("1")
time.sleep(2)
driver.close()
