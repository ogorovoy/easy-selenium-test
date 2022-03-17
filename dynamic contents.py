from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import os
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
#select = Select(driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]'))
text = description.text
print(text)


time.sleep(20)
#element="Accusantium eius ut architecto neque vel voluptatem vel nam eos minus ullam dolores voluptates enim sed voluptatem rerum qui sapiente nesciunt aspernatur et accusamus laboriosam culpa tenetur hic aut placeat error autem qui sunt."
#element = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[1]/div[2]/text()")

#print(element)
#element = driver.find_elements_by_class_name("large-10 columns")








#a = []
#b = []

#a= driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[1]/img')
#print(a)

#b = driver.find_element_by_xpath("//*[@id='content']/div[1]/div[2]/text()")
#print(b)

#driver.refresh()



driver.close()