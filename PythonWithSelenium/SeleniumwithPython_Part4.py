

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()        #To maximize a browser window


dropdown=driver.find_element(By.XPATH, "//select[@id='input-country']")

dropdowncountry=Select(dropdown)                #Select class declaration

#select dropdown:
dropdowncountry.select_by_visible_text("Iceland")
dropdowncountry.select_by_index(3)
#dropdowncountry.select_by_value(10)

#capture all the options from dropdown and print them:
alloptions=dropdowncountry.options
print(len(alloptions))                      #to print all options count in console

for opt in alloptions:                      #to print all options list in console
    print(opt.text)

#select option from dropdown without using select buildin function:
for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break

#without using select class:

alloptions=driver.find_elements(By.XPATH, "//*[@id='input-country']/option")

for opt in alloptions:              #to print all options list in console without using select class
    print(opt.text)

for opt in alloptions:              #to click option without using select class
    if opt.text=="India":
        opt.click()
        break

# #practice dropdown
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# dropdown1=Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
# dropdown1.select_by_visible_text("Faster")
















