
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()        #To maximize a browser window


#how to handle alerts and popup in a webpage

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

alertwindow=driver.switch_to.alert          #ALERT class declaration

print(alertwindow.text)                     #print text in alert using text method
alertwindow.send_keys("Nagarajan")          #input text to alert using send_keys() method
alertwindow.accept()                        #click ok button using accept() method
alertwindow.dismiss()                       #click cancel button using dismiss() method

#how to handle Authentication popups:

#syntax:
#http://username:password@URL

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")





















