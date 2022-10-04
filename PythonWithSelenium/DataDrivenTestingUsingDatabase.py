import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(20)


con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="studentDB")      #establish connection with MySQL database
cursor=con.cursor()             #establish cursor() function and saved in one variable to use furthur
cursor.execute("select * from FixedDeposits")



for row in cursor:
    #get datas from database using MySQL database connection:

    principle=row[0]        #capture datas from database row by row and saved in variable
    ROI=row[1]
    period1=row[2]
    period2=row[3]
    frequency=row[4]
    exp_mvalue=row[5]

    #passing datas to the web application :
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)           #send the captured datas here through the varibale we stored above
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)
    Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']")).select_by_visible_text(period2)
    Select(driver.find_element(By.XPATH,"//select[@id='frequency']")).select_by_visible_text(frequency)
    driver.execute_script("arguments[0].click()",driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img"))

    actual_mvalue=driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text

    #Now validation the datas with expected and actual datas:
    if float(exp_mvalue)==float(actual_mvalue):                 #convert string values into float becoz values in decimal format
        print("test passed")
    else:
        print("test failed")
    driver.execute_script("arguments[0].click()",driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img"))
con.close()         #database connection need to close here


time.sleep(6)
driver.close()








