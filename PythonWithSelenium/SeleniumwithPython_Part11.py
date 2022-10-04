#How to download files in chrome, firefox, and edge browsers


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os                           #import module for return current working path or location
location=os.getcwd()                #return current working path or location





#setting for chrome browser download in our desired path:
def chromesetup():
    from selenium.webdriver.chrome.service import Service as ChromeService  # To import chrome browser module (new version)
    from webdriver_manager.chrome import ChromeDriverManager  # To import chrome browser module (new version)

    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
    return driver

#=======================================================================================================================

#setting for edge browser download in our desired path:
def edgesetup():
    from selenium.webdriver.edge.service import Service as EdgeService  # To import chrome browser module (new version)
    from webdriver_manager.microsoft import EdgeChromiumDriverManager  # To import chrome browser module (new version)

    preferences={"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=ops)
    return driver

#=======================================================================================================================

#setting for firefox browser download in our desired path:
def firefoxsetup():
    from selenium.webdriver.firefox.service import Service as FirefoxService  # To import chrome browser module (new version)
    from webdriver_manager.firefox import GeckoDriverManager  # To import chrome browser module (new version)

    preferences={"download.default_directory":location}
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisl","application/msword")           #here mime type to mention (ex: word ==application/msword)
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2)         #0--for saving in desktop, 1--for saving in downloads folder, 2--for saving in our desired location
    ops.set_preference("browser.download.dir",location)         #location where we need to save
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)
    return driver



driver=chromesetup()        #this is to invoke chromesetup
driver=edgesetup()        #this is to invoke edgesetup
driver=firefoxsetup()        #this is to invoke firefoxsetup


driver.get("https://www.leafground.com/file.xhtml;jsessionid=node01fmqgpzw10ow71doqxcjf3z514349064.node0")
driver.maximize_window()        #To maximize a browser window
driver.implicitly_wait(10)


#download using chrome browser:

#this is coding part:
button=driver.find_element(By.XPATH,"//span[normalize-space()='Download']")
driver.execute_script("arguments[0].scrollIntoView();",button)
driver.execute_script("arguments[0].click()",button)




time.sleep(5)
driver.close()


































