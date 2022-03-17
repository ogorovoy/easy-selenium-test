from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

driver.find_element_by_link_text("Inputs").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='content']/div/div/div/input").send_keys("123456789")
time.sleep(3)
driver.close()

