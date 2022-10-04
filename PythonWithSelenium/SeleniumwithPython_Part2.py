
#work with checkboxes

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("http://testleaf.herokuapp.com/pages/checkbox.html")
driver.maximize_window()        #To maximize a browser window

#select checkboxes having more than one:
checkbox=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
len(checkbox)

#method 1:
for i in range(len(checkbox)):
    checkbox[i].click()
#method 2:
for i in checkbox:
    checkbox.click()

#method 3:
for i in checkbox:
    languagename=checkbox.get_attribute('id')
    if languagename=="java":
        checkbox.click()

#method 4: To select last 2 or 3 checkboxes scenario
for i in range(len(checkbox)-2,len(checkbox)):    #range() is totallength-2, totallength
    checkbox[i].click()