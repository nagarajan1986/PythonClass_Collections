


import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService  # To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager  # To import chrome browser module (new version)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://testleaf.herokuapp.com/")
driver.maximize_window()        #To maximize a browser window
driver.implicitly_wait(10)


#how to handle bootstrap dropdown:

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countrieslist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")       #this commmon xpath for all list available

print(len(countrieslist))

time.sleep(5)
for country in countrieslist:           #read all list from the dropdown and get selected by our desired one
    if country.text=="India":
        country.click()
        break


#How to take Screenshot:

#method 1:
driver.save_screenshot("C:\\Users\\Admin\\Desktop\\new_python_project\\PythonWithSelenium\\image.png")
#or
#driver.save_screenshot(os.getcwd()+"\\image.png")          #another way to avoid long path
#
# #method 2:
driver.get_screenshot_as_file(os.getcwd()+"\\image.png")

#method 3:
driver.get_screenshot_as_png()
driver.get_screenshot_as_base64()           #both are binary format (ASCII code). we dont need this for framework stage

#How to open browser window in new tab:
driver.find_element(By.XPATH,"(//a[@class='wp-categories-link maxheight'])[1]").send_keys(Keys.CONTROL+Keys.ENTER)

#Selenium 4 stuffs new:
#open browser window in new tab and swithches to new tab automatically:

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.switch_to.new_window('tab')                #this command will open new browser tab
driver.get("http://testleaf.herokuapp.com/")

#open browser window and swithches to new window automatically:
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.switch_to.new_window('window')                #this command will open new browser window
driver.get("http://testleaf.herokuapp.com/")








time.sleep(5)
driver.close()


































