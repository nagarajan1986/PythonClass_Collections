import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)

#Notification Popup:
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)            #To import chrome browser module (new version)




driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()        #To maximize a browser window

#==============================================================================================================

# WebTable:

#calculating rows & columns:
noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcolumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(noofrows)
print(noofcolumns)

#Read specific rows & columns:
print(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text)

#Read all specific rows & columns:

for r in range(2,noofrows+1):
    for c in range(1,noofcolumns+1):
        data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text  #syntax for getting all rows & column
        print(data, end='   ')          #print data and give spaces syntax
    print()

#Read mukesh author name column and get his book name and price datas:
for r in range(2,noofrows+1):
    authorname=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text      #first, we need to find author name
    if authorname=="Mukesh":        #match with authorname if matches get bookname and price
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text      #get mukesh author  bookname
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text         #get mukesh author  book price
        print(bookname,"    ",authorname,"     ", price)





driver.close()


































