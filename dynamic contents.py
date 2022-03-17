from selenium import webdriver
import time


PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

driver.find_element_by_link_text("Dynamic Content").click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/img')
photo = '//*[@id="content"]/div[1]/div[1]/img'
print(photo)

description = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]')
text = description.text
print(text)


time.sleep(20)
driver.close()