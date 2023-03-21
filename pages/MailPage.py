import json

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


from .BasePage import BasePage
from locators import Mail
from common import common

import time


class MailPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.subject_of_letter = None
        self.body_of_letter = None
        self.all_letters = dict()
        self.letter_dict_to_json = None

    def letter_dict_to_json(self, d):
        self.letter_dict_to_json = json.dumps(d)
        return self.letter_dict_to_json

    def send_new_letter(self):
        self.create_new_letter_button_click()
        self.field_to_field_input()
        self.field_subject_input(common.random_string())
        self.switch_to_body_letter_frame()
        self.field_body_letter(common.random_string())
        self.back_to_default_web_page_frame()
        self.send_button_click()
        self.check_send_msg_ready()
        self.repeat_send_button_click()

    def send_letter_on_theme(self):
        self.create_new_letter_button_click()
        dict_data_letters = common.read_from_json()

        for (title, body) in dict_data_letters.items():
            self.field_to_field_input()
            self.field_subject_input(f"Received mail on theme {title}")
            self.switch_to_body_letter_frame()
            self.field_body_letter(f"Received mail on theme {title} with message: {body}. "
                                   f"It contains {common.calc_symbol_in_strint(body,'letter')} letters "
                                   f"and {common.calc_symbol_in_strint(body,'number')} numbers")
            self.back_to_default_web_page_frame()
            self.send_button_click()
            self.check_send_msg_ready()
            self.repeat_send_button_click()

    def create_new_letter_button_click(self):
        new_letter = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.SideBar.NEW_LETTER))
        new_letter.click()

    def sent_letter_button_click(self):
        sent_letter = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.SideBar.SENT_LETTERS))
        sent_letter.click()

    def incoming_letter_button_click(self):
        incoming_letter = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.Modal.INCOMING_LETTERS))
        incoming_letter.click()

    def sent_letter_button_text(self):
        WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.SideBar.SENT_LETTERS))

    def switch_to_body_letter_frame(self):
        elements = self.browser.find_elements(By.TAG_NAME, "iframe")
        self.browser.switch_to.frame(elements[1].get_attribute("id"))

    def back_to_default_web_page_frame(self):
        self.browser.switch_to.default_content()

    def field_to_field_input(self):
        to_field = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.Screens.TOFIELDINPUT))
        to_field.click()
        to_field.clear()
        to_field.send_keys(self.LOGIN_ENV + "@ukr.net")

    def field_subject_input(self, subject_string):
        subject = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable(Mail.Content.Screens.SUBJECT))
        subject.click()
        subject.clear()
        self.subject_of_letter = subject_string
        subject.send_keys(self.subject_of_letter)

    def field_body_letter(self, body_string):
        body_letter = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable(Mail.Content.Screens.BODY_LETTER))
        body_letter.click()
        body_letter.clear()
        self.body_of_letter = body_string
        body_letter.send_keys(self.body_of_letter)
        self.all_letters[self.subject_of_letter] = self.body_of_letter

    def send_button_click(self):
        send_button = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable(Mail.Content.Screens.SEND_BUTTON))
        send_button.click()

    def check_send_msg_ready(self):
        WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable(Mail.Content.Screens.SENDING_MSG_READY))

    def repeat_send_button_click(self):
        repeat_send_button = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable(Mail.Content.Screens.REPEAT_SEND_LETTER))
        repeat_send_button.click()

    def find_letter(self):
        dict_data_letters = common.read_from_json()

        for (title, body) in dict_data_letters.items():
            self.search_input_click()
            self.search_more_click()
            contains_input = WebDriverWait(self.browser, self.delay).until(
                EC.element_to_be_clickable(Mail.Content.Modal.CONTAINS_INPUT))
            modal_submit_button = WebDriverWait(self.browser, self.delay).until(
                EC.element_to_be_clickable(Mail.Content.Modal.MODAL_SUBMIT_BUTTON))
            contains_input.click()
            contains_input.clear()
            contains_input.send_keys(title)
            modal_submit_button.click()

            subject_letter = WebDriverWait(self.browser, self.delay).until(
                EC.presence_of_all_elements_located(Mail.Content.Modal.SUBJECT_OF_LETTER))

            assert self.browser.find_element(*Mail.Content.Modal.INCOMING_LETTERS_TEXT).text in \
                   [i.text for i in subject_letter], "Немає листів у папці Вхідні"
            assert self.browser.find_element(*Mail.Content.Modal.SENT_LETTERS_TEXT).text in \
                   [i.text for i in subject_letter], "Немає листів у папці Надіслані"

    def search_input_click(self):
        search_input = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable(Mail.Content.Header.SEARCH_INPUT))
        search_input.click()

    def search_more_click(self):
        search_more = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.Header.SEARCH_MORE))
        search_more.click()

    def click_all_checkboxes(self):
        all_checkboxes = WebDriverWait(self.browser, self.delay).until(
            EC.visibility_of_all_elements_located(Mail.Content.Screens.ALL_CHECKBOXES))
        # [i.click() for i in all_checkboxes]
        for item in range(int(self.NUMOFLETTERS_ENV)-1):
            all_checkboxes[item].click()

    def delete_button_click(self):
        WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Mail.Content.Screens.DELETE_BUTTON)).click()









