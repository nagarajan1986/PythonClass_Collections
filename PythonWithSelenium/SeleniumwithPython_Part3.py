# working with links
# 1. internal links
# 2. external links
# 2. broken links

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))            #To import chrome browser module (new version)


driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()        #To maximize a browser window

#internal links:
# click on link:
# driver.find_element(By.LINK_TEXT, "Go to Home Page").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Go to").click()

#find number of links in a page:
# links=driver.find_elements(By.TAG_NAME, "a")
# # links=driver.find_elements(By.XPATH, "//a")       #to find links using xpath also as "//a"
# print(len(links))

#print all the link names:
# for i in links:
#     print(i.text)

#we need to install requests module package through file-->settings--->python interpreter-->requests
#find broken links:
alllinks=links=driver.find_elements(By.TAG_NAME, "a")
count=0                                 #declaring count variable initially as zero

for link in alllinks:
    url=link.get_attribute('href')      #collecting all links by using href tag
    try:                                #some exception will occcur while running script, so we kept coding in try except block
        res=requests.head(url)          #send some request with those links and get response and saved with one variable
    except:
        None
    if res.status_code>=400:            #match status code with above 400 means, it is broken link
        print(url, " is broken link")   #print those broken link
        count+=1                        #count those broken link and saved in count variable that we declare before
    else:
        print(url, " is valid link")    ##match status code with below 400 means, it is valid link

print("Total number of broken link : ", count)          #finally print those broken link count with help of that count variable










