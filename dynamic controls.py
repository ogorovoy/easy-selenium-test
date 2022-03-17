from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

driver.find_element_by_link_text("Dynamic Controls").click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="checkbox"]/input').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="checkbox-example"]/button').click()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="input-example"]/button').click()
time.sleep(8)

driver.find_element_by_xpath('//*[@id="input-example"]/input').click()
driver.find_element_by_xpath('//*[@id="input-example"]/input').send_keys('depressio')
driver.find_element_by_xpath('//*[@id="input-example"]/button').click()
time.sleep(6)
driver.close()