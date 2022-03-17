from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import os
import time


PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

driver.find_element_by_link_text("Inputs").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='content']/div/div/div/input").send_keys("123456789")
#driver.find_element_by_class_name("example").send_keys("3")
#upload_field = driver.find_element_by_partial_link_text('number')
#upload_field.clear()
#upload_field.send_keys("3")
#driver.find_element_by_type("number").send_keys("3")
time.sleep(3)
driver.close()

