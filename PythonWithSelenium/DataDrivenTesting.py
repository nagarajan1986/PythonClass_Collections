import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from PythonWithSelenium import ExcelUtils

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(20)

file="D:\Demofiles\DataDriven_Python.xlsx"

rows=ExcelUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #get datas from excel sheet using ExcelUtils (read excel function) file where we already defined all functions:

    principle=ExcelUtils.readData(file,"Sheet1",r,1)
    ROI=ExcelUtils.readData(file, "Sheet1", r, 2)
    period1=ExcelUtils.readData(file, "Sheet1", r, 3)
    period2=ExcelUtils.readData(file, "Sheet1", r, 4)
    frequency=ExcelUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue=ExcelUtils.readData(file, "Sheet1", r, 6)

    #passing datas to the web application :
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)
    Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']")).select_by_visible_text(period2)
    Select(driver.find_element(By.XPATH,"//select[@id='frequency']")).select_by_visible_text(frequency)
    driver.execute_script("arguments[0].click()",driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img"))

    actual_mvalue=driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text

    #Now validation the datas with expected and actual datas:
    if float(exp_mvalue)==float(actual_mvalue):                 #convert string values into float becoz values in decimal format
        print("test passed")
        ExcelUtils.writeData(file,"Sheet1",r,8,"Passed")
        ExcelUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        ExcelUtils.writeData(file, "Sheet1", r, 8, "Failed")
        ExcelUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.execute_script("arguments[0].click()",driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img"))


time.sleep(6)
driver.close()








