
# 1. driver.switch_to.frame("name of the frame")
# 2. driver.switch_to.frame("id of the frame")
# 3. driver.switch_to.frame("Webelement")
# 4. driver.switch_to.frame(index)

#driver.switch_to.default_content()


import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()        #To maximize a browser window


#how to frames or iframes in a webpage:

driver.switch_to.frame("packageListFrame")                          #syntax for switch into frames
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()    #webelements in the frames
driver.switch_to.default_content()                                  #syntax for go back to the main frame

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//div[@class='topNav']//a[normalize-space()='Help']")

print("Successfully clicked elements into the frames!!!!!!!")


#other scenario with iframes:
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
outframe=driver.find_element(By.XPATH, "/html/body/section/div")
driver.switch_to.frame(outframe)

innerframe=driver.find_element(By.XPATH, "/html/body/section/div/div")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("welcome")

driver.switch_to.parent_frame()                 #directly switching into parent frame.

























