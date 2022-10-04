

*** Settings ***
Library    SeleniumLibrary



*** Variables ***


*** Test Cases ***
FirstTestCase:
    open browser    http://testleaf.herokuapp.com/pages/Dropdown.html    chrome
    maximize browser window

    click element    xpath://select[@id='dropdown1']
    select from list by index    3
    select from list by index    3













*** Keywords ***



