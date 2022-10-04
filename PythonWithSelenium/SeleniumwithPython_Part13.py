


#Headless mode settings for chrome, edge, and firefox:

import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService  # To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager  # To import chrome browser module (new version)

#setting for chrome browser for running script in headless mode:

def headless_chrome():
    from selenium.webdriver.chrome.service import Service as ChromeService  # To import chrome browser module (new version)
    from webdriver_manager.chrome import ChromeDriverManager  # To import chrome browser module (new version)
    ops=webdriver.ChromeOptions()
    ops.headless=True                                       #this is command for headless mode setup from ChromeOptions() class
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
    return driver

#=======================================================================================================================

#setting for edge browser for running script in headless mode:

def headless_edge():
    from selenium.webdriver.edge.service import Service as EdgeService  # To import chrome browser module (new version)
    from webdriver_manager.microsoft import EdgeChromiumDriverManager  # To import chrome browser module (new version)
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=ops)
    return driver

#=======================================================================================================================

#setting for firefox browser for running script in headless mode:

def headless_firefox():
    from selenium.webdriver.firefox.service import Service as FirefoxService  # To import chrome browser module (new version)
    from webdriver_manager.firefox import GeckoDriverManager  # To import chrome browser module (new version)
    ops=webdriver.FirefoxOptions()
    ops.headless=True
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)
    return driver



driver=headless_chrome()        #this is to invoke chromesetup
driver=headless_edge()        #this is to invoke edgesetup
driver=headless_firefox()        #this is to invoke firefoxsetup


driver.get("http://testleaf.herokuapp.com/")
driver.maximize_window()        #To maximize a browser window
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)













time.sleep(5)
driver.close()


































