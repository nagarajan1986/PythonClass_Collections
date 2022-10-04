import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()        #To maximize a browser window


#Window handling:
windId=driver.current_window_handle                 #syntax: to get single window id
print(windId)
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

allwindid=driver.window_handles                     #syntax: to get all window id's
print(allwindid)

#Approach 1:
parentid=allwindid[0]
childid=allwindid[1]

driver.switch_to.window(childid)                    #Switch to window syntax
print("Title of the child window",driver.title)

driver.switch_to.window(parentid)
print("Title of the parent window",driver.title)



#Approach 2:
for winid in allwindid:
    driver.switch_to.window(winid)
    print(driver.title)

for winid in allwindid:                              #SYNTAX: Switch to window for our desired windows if we have more than 1 or 2......
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM" or driver.title=="OrangeHRM":
        driver.close()


#practice window handling:
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Selenium in biology']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Selenium (software)']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Selenium disulfide']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Selenium dioxide']").click()
#
# allwindowid=driver.window_handles
#
# for windowid in allwindowid:
#     driver.switch_to.window(windowid)
#     print(driver.title)






























