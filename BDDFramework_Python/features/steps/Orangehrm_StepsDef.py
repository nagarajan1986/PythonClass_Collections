
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from allure_behave.hooks import allure_report



@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("http://www.testyou.in/Login.aspx")

@when('user enter username "{user}" and password "{pwd}"')
def usernameAndPassword(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@id='ctl00_CPHContainer_txtUserLogin']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@id='ctl00_CPHContainer_txtPassword']").send_keys(pwd)

@then('user hit login button')
def loginButton(context):
    context.driver.find_element(By.XPATH,"//input[@id='ctl00_CPHContainer_btnLoginn']").click()

@then('user must see the error with wrong credentials')
def loginButton(context):
    text=context.driver.find_element(By.XPATH,"//span[text()='Userid or Password did Not Match !!']").text
    assert text=="Userid or Password did Not Match !!"

@then('close browser')
def closeBrowser(context):
    context.driver.close()

#allure_report("C:\\Users\\Admin\\Desktop\\new_python_project\\BDDFramework_Python\\Allure-reporting")



