#This is our Test Case

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service   #To import chrome browser module

serv_obj=Service("C:\Drivers\chromedriver.exe")         #To import chrome browser module
driver=webdriver.Chrome(service=serv_obj)               #To import chrome browser module

driver.get("https://letcode.in/")
driver.maximize_window()        #To maximize a browser window

driver.find_element(By.XPATH,"//a[text()='Log in']").click()
driver.find_element(By.NAME,"email").send_keys("nagu.tcl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()

links=driver.find_elements(By.TAG_NAME, "a") #To find total links in a webpage
print(links)
print(len(links))

actual_title=driver.title                       #To url title verification / validation
expected_title="LetCode with Koushik"

if actual_title==expected_title:
    print("Test Case Passed")
else:
    print("Test Case Failed")

driver.close()