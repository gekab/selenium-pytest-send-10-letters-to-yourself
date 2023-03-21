from selenium.webdriver.common.by import By


class Main:
    class Header:
        SEARCH = (By.ID, "search-input")
        SUBMIT = (By.CSS_SELECTOR, "[type='submit']")

    class LeftSide:
        class LoginFrame:
            LOGIN_FORM = (By.ID, "login-frame-wraper")
            LOGIN_FRAME = "mail widget"
            LOGIN = (By.CSS_SELECTOR, "[name='login']")
            PASSWORD = (By.CSS_SELECTOR, "[name='password']")
            SUBMIT = (By.CSS_SELECTOR, "[type='submit']")
            ENTRY_MAIL = (By.CSS_SELECTOR, "[class='service__entry service__entry_mail']")
