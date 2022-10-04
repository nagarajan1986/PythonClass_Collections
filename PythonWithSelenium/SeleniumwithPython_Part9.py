#Actions class
#ActionChains
# movetoelement
# doubleclick
# rightclick
# draganddrop
# sliders


import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()        #To maximize a browser window
driver.implicitly_wait(10)

#using ActionChains class, move_to_element (Mouse Hover actions)
primebtn=driver.find_element(By.XPATH,"//span[text()='Prime']")
act=ActionChains(driver)
act.move_to_element(primebtn).perform()
driver.find_element(By.XPATH,"//img[@id='multiasins-img-link']").click()

#doubleclick
text=driver.find_element(By.XPATH,"//input[@id='field1']")
text.clear()
text.send_keys("Nagarajan")
copybtn=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

time.sleep(5)
act=ActionChains(driver)
act.double_click(copybtn).perform()
time.sleep(5)

#rightclick

copybtn=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act=ActionChains(driver)
act.context_click(copybtn).perform()

time.sleep(5)

#Drag and drop:
source=driver.find_element(By.XPATH,"//p[text()='Drag me to my target']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")

# source=driver.find_element(By.XPATH,"//img[@alt='the peaks of high tatras']")
# target=driver.find_element(By.XPATH,"//div[@id='trash']")

source1=driver.find_element(By.XPATH,"//img[@alt='The chalet at the Green mountain lake']")
target1=driver.find_element(By.XPATH,"//div[@id='trash']")

act=ActionChains(driver)
act.drag_and_drop(source,target).perform()
act.drag_and_drop(source1,target1).perform()


time.sleep(5)

#Sliders:

slider=driver.find_element(By.XPATH,"//*[@id='slider']/span")
print(slider.location)  #{'x': 1012, 'y': 1373}   #here x is mean by horizontal, y means by vertical

act=ActionChains(driver)
act.drag_and_drop_by_offset(slider,100,0).perform()

print(slider.location)      #{'x': 1113, 'y': 1373}

time.sleep(5)

#Scrolling down page by some pixel: (javascript)
driver.execute_script("window.scrollBy(0,3000)","")                 #javascript syntax need to boycott
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ",value)     #2130

#scrolling till the element we mentioned is visible:
substxt=driver.find_element(By.XPATH,"//*[@id='Blog1']/div[4]/div")
driver.execute_script("arguments[0].scrollIntoView();",substxt)       #scrolling until we desired element visible

#scroll down the page till end of webpage:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")      #javascript syntax need to boycott

#scroll up the page in a webpage:
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")      #javascript syntax need to boycott


time.sleep(5)
driver.close()


































