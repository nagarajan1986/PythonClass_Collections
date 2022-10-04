#different xpath axes when dynamic locators occurs:
# self
# parent
# child
# following
# preceding
# following-sibling
# preceding-sibling
# ancestor
# descendent

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("https://money.rediff.com/gainers")
driver.maximize_window()        #To maximize a browser window

#self
text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/self::a").text
print(text_msg)

#parent
text_msg1=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/parent::td").text
print(text_msg1)

#child
text_msg2=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/ancestor::tr/child::td").text   #since self element has no child so we traverse to ancestor and child of ancestor
print(text_msg2)

#Ancestor
text_msg3=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/ancestor::tr").text
print(text_msg3)

#descendant
text_msg4=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/descendant::*").text
print(text_msg4)

#following
text_msg5=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/following::*").text
print(text_msg5)

#following-sibling
text_msg6=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/following-sibling::*").text
print(text_msg6)

#preceding
text_msg6=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/preceding::*").text
print(text_msg6)

#preceding-sibling
text_msg6=driver.find_element(By.XPATH, "//a[contains(text(),'Flex Foods')]/preceding-sibling::*").text
print(text_msg6)




driver.close()