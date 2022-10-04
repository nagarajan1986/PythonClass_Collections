#Keyboard actions


import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)

driver.get("https://text-compare.com/")
driver.maximize_window()        #To maximize a browser window
driver.implicitly_wait(10)

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium with python")

time.sleep(5)
#input1===> Ctrl+A select text
act=ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

#input1===> Ctrl+C copy text
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

#input1--->input2===>press tab key
act.send_keys(Keys.TAB).perform()

#input2===> Ctrl+V paste text
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()


time.sleep(5)
driver.close()


































