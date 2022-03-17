from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import os
import time
import csv

#------------ SETTINGS ---------------#

sett_pid = "Store_name"
sett_user_name = "User_name"
sett_password = "User_password"
sett_location_file = "file_name.file_format"
sett_order_id_row_name = "ORDER_ID"
sett_track_nr_row_name = "TRACK_NR"


#------------ END SETTINGS ------------#

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://plentymarkets-cloud-de.com/")
wait = WebDriverWait(driver, 10)

time.sleep(2)

pid = driver.find_element_by_id("pid")
usr = driver.find_element_by_id("username")
pas = driver.find_element_by_id("password")
log_btn = driver.find_element_by_xpath("//*[@id='loginForm']/button")

time.sleep(2)

pid.send_keys(sett_pid)
usr.send_keys(sett_user_name)
pas.send_keys(sett_password)
log_btn.click()

time.sleep(4)

driver.get(driver.current_url.replace("/terra/start/dashboard","/admin/gui_call.php?Object=mod_order/fulfillment@GuiFulfillment&Params[gui]=&action=&no_subtitle=1&is_client=0&is_terra=1&is_gwt=1#importPaketNumberPaneBaseId"))

time.sleep(2)

list_size = Select(driver.find_element_by_xpath("//*[@id='listSelectFormId']"))
list_size.select_by_visible_text("150")

time.sleep(2)

a=1
print("The contents of the above file is as follows:")
with open(sett_location_file) as c:
    r = csv.DictReader(c)
    for row in r:
        driver.find_element_by_id("PlentyGuiFormText_"+str(a)+"_id").send_keys(str(row[sett_order_id_row_name]))
        a=a+1
        driver.find_element_by_id("PlentyGuiFormText_"+str(a)+"_id").send_keys(str(row[sett_track_nr_row_name]))
        a=a+1

print("THE END ")
print("check and accept")
os.system("pause")
