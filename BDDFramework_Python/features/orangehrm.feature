  Feature: TestYou Login Page
    Scenario Outline: Login page in application
        Given launch chrome browser
        When user enter username "<username>" and password "<password>"
        Then user hit login button
        Then user must see the error with wrong credentials
        And close browser


    Examples:
        | username | password |
        | nagu.tcl@gmail.com | admin1234 |
        | naga.tcl@gmail.com | admin12345 |
        | nagaraj.tcl@gmail.com | admin123567 |
        | nagarajan.tcl@gmail.com | admin123897 |