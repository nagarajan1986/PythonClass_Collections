#This is our Test Case

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("http://testleaf.herokuapp.com/pages/Edit.html")
driver.maximize_window()        #To maximize a browser window


driver.find_element(By.ID,"email").send_keys("nagu.tcl@gmail.com")
ourtext=driver.find_element(By.ID,"email").get_attribute('value')     # get_attribute('value') is used for getAttribute function for getting our entered text
print(ourtext)
driver.find_element(By.XPATH, "//input[@value='Append ']").send_keys(" admin123")
ourtext1=driver.find_element(By.XPATH, "//input[@value='Append ']").get_attribute('value')
print(ourtext1)
text=driver.find_element(By.XPATH, "//input[@value='Clear me!!']").get_dom_attribute('value')   # get_dom_attribute('value') is used for gettext function
print(text)
enable=driver.find_element(By.XPATH, "//input[@disabled='true']").is_enabled()
print(enable)

links=driver.find_elements(By.TAG_NAME, "a") #To find total links in a webpage
print(links)
print(len(links))

# actual_title=driver.title                       #To url title verification / validation
# expected_title="OrangeHRM"
#
# if actual_title==expected_title:
#     print("Test Case Passed")
# else:
#     print("Test Case Failed")

driver.close()