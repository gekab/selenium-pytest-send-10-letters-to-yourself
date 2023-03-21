from selenium.webdriver.common.by import By


class Mail:
    class TopBanner:
        pass

    class Content:
        class SideBar:
            NEW_LETTER = (By.CLASS_NAME, "button.primary.compose")
            INBOX_LISTS = (By.CLASS_NAME, "sidebar__list inbox")
            SENT_LETTERS = (By.ID, "10001")
            SENT_LETTERS_TEXT = (By.CSS_SELECTOR, "[id='10001'] > span.sidebar__list-link-name")

        class Header:
            SEARCH_INPUT = (By.CSS_SELECTOR, "div.search input")
            SEARCH_MORE = (By.CSS_SELECTOR, "a.search__more")

        class Modal:
            CONTAINS_INPUT = (By.CSS_SELECTOR, "input[name='contains']")
            FOLDERS_BUTTON = (By.CSS_SELECTOR, "a[class='search-advanced__folders-button']")
            # FOLDERS_LIST = (By.CSS_SELECTOR, "[class='search-advanced__folders']")
            INCOMING_LETTERS_TEXT = (By.CSS_SELECTOR, "[id='0'] > span.sidebar__list-link-name")
            SENT_LETTERS_TEXT = (By.CSS_SELECTOR, "[id='10001'] > span.sidebar__list-link-name")
            INCOMING_LETTERS = (By.CSS_SELECTOR, "a.inbox span.sidebar__list-link-name")
            SENT_LETTERS = (By.XPATH, "//a[contains(text(),'Надіслані')and @class]")
            SUBJECT_OF_LETTER = (By.CSS_SELECTOR, "td.msglist__row-subject > a.msglist__row-label")
            MODAL_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[class='default button primary']")
            ALL_RECORDS_ONE_MORE_LETTER = (By.CSS_SELECTOR, "[class='msglist__row-label']")

        class Screens:
            TOFIELDINPUT = (By.CSS_SELECTOR, "[class='input'][name='toFieldInput']")
            SUBJECT = (By.CSS_SELECTOR, "[class='input'][name='subject']")
            BODY_LETTER_FRAME = "mce_0_ifr"
            BODY_LETTER = (By.ID, "tinymce")
            SEND_BUTTON = (By.CSS_SELECTOR, "[class='controls'] [class='button primary send']")
            SENDING_MSG_READY = (By.CSS_SELECTOR, "[class='sendmsg__ads-ready']")
            REPEAT_SEND_LETTER = (By.CSS_SELECTOR, "[class='button primary']")
            ALL_CHECKBOXES = (By. CSS_SELECTOR, "tbody td.msglist__row-check")
            DELETE_BUTTON = (By.CSS_SELECTOR, "a.remove")
