import time     #time.sleep import module

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC        #explict wait import command

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)

from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("http://testleaf.herokuapp.com/pages/checkbox.html")
driver.maximize_window()        #To maximize a browser window

#Application commands:
print(driver.title)     #to get current url title       #TestLeaf - Selenium Playground
print(driver.current_url)       #to get current url     #http://testleaf.herokuapp.com/
#print(driver.page_source)       #to get current url page source (i.e., full html/xml structure)

#Conditonal commands:
print(driver.find_element(By.XPATH, "//div[@id='contentblock']//div[2]").is_enabled())
print(driver.find_element(By.XPATH, "//label[normalize-space()='Confirm Selenium is checked']").is_selected())
print(driver.find_element(By.XPATH, "//div[@id='contentblock']//div[2]").is_displayed())

#Navigational commands:
driver.back()           # browser will back to previous website
driver.forward()        # browser will back to forward website
driver.refresh()         # browser will refresh the page

#findelements with single or multiple webelement example
#Method 1:
elements=driver.find_elements(By.XPATH, "//div[@id='contentblock']//div[2]")
print(len(elements))
print(elements[0].text)   #to get particular element text
elements[0].send_keys()     #by changing index number we can access individual
elements[0].click()

#Method 2:
for ele in elements:
    print(ele.text)     #to get all webelement text

#difference between text, get_attribute('value'), get_dom_attribute('value')
driver.find_element(By.XPATH, "//div[@id='contentblock']//div[2]").text         #to get webpage text
driver.find_element(By.XPATH, "//div[@id='contentblock']//div[2]").get_attribute('value')   #to get our input text in textbox we send
driver.find_element(By.XPATH, "//div[@id='contentblock']//div[2]").get_dom_attribute('value')    #to get attribute value in webpage

#wait commands or synchronization: #implicit wait explicit wait
time.sleep(5)           #it is jus a pause command not like wait command. it is python command not selenium

#implicit wait:
driver.implicitly_wait(10)  #implicit wait and give time as seconds.

#explicit wait:
#it works based on the condition not based on time we give
#from selenium.webdriver.support import expected_conditions as EC        #explict wait import command

explicitwait=WebDriverWait(driver,10)       #explicit wait declaration
element=explicitwait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='contentblock']//div[2]")))

explicitwait=WebDriverWait(driver,10, ignored_exceptions=[Exception])       #explicit wait declaration to ignore exception

explicitwait1=WebDriverWait(driver,10, poll_frequency=2, ignored_exceptions=[Exception])  #explicit wait declaration to poll frequency we can give








driver.close()