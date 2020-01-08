from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
phno=(input("enter mobile number:"))
password=input("enter password:")
search = input("Enter keyword to search")

driver=webdriver.Chrome()
driver.get('https://flipkart.com')
driver.maximize_window()
#add xpath to the chrome browser chorme lo,moptions tools lo extensions lo menu chrome web store search
#xpath ,chropath
#add to chrome
driver.find_element(By.XPATH,"//input[@class='_2zrpKA _1dBPDZ']").send_keys(phno)
driver.find_element(By.XPATH,"//input[@class='_2zrpKA _3v41xv _1dBPDZ']").send_keys(password)
driver.find_element(By.XPATH,"//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
time.sleep(15)
driver.find_element_by_class_name("LM6RPg").send_keys(search,keys.ENTER)

