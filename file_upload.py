from selenium import webdriver
import os
import time

directory_path = os.getcwd()

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(4)

driver.find_element_by_link_text("File Upload").click()
time.sleep(2)

driver.find_element_by_id("file-upload").send_keys(directory_path + "\DOBBY2.jpg")
driver.find_element_by_id("file-submit").click()
time.sleep(6)
driver.close()
