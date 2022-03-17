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
time.sleep(4)

driver.find_element_by_link_text("File Upload").click()
time.sleep(2)

driver.find_element_by_id("file-upload").send_keys("C:\\Users\\Pressio\\Downloads\\DOBBY2.jpg")
driver.find_element_by_id("file-submit").click()
time.sleep(6)
driver.close()
