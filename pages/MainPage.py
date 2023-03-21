from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
from locators import Main

import time


class MainPage(BasePage):
    def login(self):
        self.check_login_form()
        self.switch_to_frame()
        self.login_input_set_value()
        self.password_input_set_value()
        self.submit_button_click()

    def check_login_form(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(Main.LeftSide.LoginFrame.LOGIN_FORM))

    def switch_to_frame(self):
        self.browser.switch_to.frame(Main.LeftSide.LoginFrame.LOGIN_FRAME)

    def login_input_set_value(self):
        login_input = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(Main.LeftSide.LoginFrame.LOGIN))
        login_input.click()
        login_input.clear()
        login_input.send_keys(self.LOGIN_ENV)

    def password_input_set_value(self):
        password_input = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(Main.LeftSide.LoginFrame.PASSWORD))
        password_input.click()
        password_input.clear()
        password_input.send_keys(self.PASSWD_ENV)

    def submit_button_click(self):
        submit_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(Main.LeftSide.LoginFrame.SUBMIT))
        submit_button.click()

    def entry_mail_link_is_located(self):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(Main.LeftSide.LoginFrame.ENTRY_MAIL))

    def entry_mail_link_click(self):
        entry_mail_link = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(Main.LeftSide.LoginFrame.ENTRY_MAIL))
        entry_mail_link.click()

    def switch_to_msglist_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert '#msglist' in self.browser.current_url


