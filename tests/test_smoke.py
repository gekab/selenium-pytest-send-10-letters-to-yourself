from selenium.webdriver.common.by import By

import pytest
import time

from pages import MainPage
from pages import MailPage
from common import common


# @pytest.mark.skip
# @pytest.mark.usefixtures("browser")
class TestMain:
    # @pytest.mark.skip
    def test_guest_can_register(self, browser):
        #  1.	Login to any email box.
        main_page = MainPage(browser)
        main_page.login()

    def test_guest_can_entry_mail(self, browser):
        #  1.1.	Switch to mail page.
        main_page = MainPage(browser)
        main_page.entry_mail_link_click()
        main_page.switch_to_msglist_window()

    # @pytest.mark.skip
    def test_guest_can_send_new_letter(self, browser):
        #  2.	Send from 10 mails from current box to yourself with:
        # •	Theme: Random string with 10 symbols (letters and numbers only)
        # •	Body: Random string with 10 symbols (letters and numbers only)
        mail_page = MailPage(browser)
        [mail_page.send_new_letter() for i in range(int(mail_page.NUMOFLETTERS_ENV))]

        # 4.	Collect data from all incoming mails and save it as Object (Dictionary), where:
        # •	Key is theme of mail
        # •	Value is body of mail
        common.json_to_file(mail_page.all_letters)

    # @pytest.mark.skip
    def test_check_letters(self, browser):
        #  3.	Check that all 10 mails are delivered.
        mail_page = MailPage(browser)
        mail_page.sent_letter_button_click()
        mail_page.find_letter()

    # @pytest.mark.skip
    def test_send_collected_data(self, browser):
        # 5.	Send collected data to yourself as: “Received mail on theme {Theme} with message: {Body}.
        # It contains {Count of letters} letters and {Count of numbers} numbers” (repeat for each mail).
        mail_page = MailPage(browser)
        mail_page.send_letter_on_theme()

    # @pytest.mark.skip
    def test_delete_all_received_mails_except_the_last_one(self, browser):
        # 6.	Delete all received mails except the last one.
        mail_page = MailPage(browser)
        mail_page.incoming_letter_button_click()
        mail_page.click_all_checkboxes()
        mail_page.delete_button_click()


@pytest.mark.skip
def test_1(browser):
    browser.get("https://www.ukr.net/")
    h2_titles = browser.find_elements(By.CSS_SELECTOR, "[class='feed__section--title']")
    print(len(h2_titles))
    print([i.text for i in h2_titles])
    for el in h2_titles:
        print(f"============={el.text}=============")
    assert "Економіка" in [i.text for i in h2_titles], "Неамєє"

