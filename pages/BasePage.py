from common import common


class BasePage:

    def __init__(self, browser):
        self.LOGIN_ENV, self.PASSWD_ENV, self.NUMOFLETTERS_ENV = ' '.join(list(common.get_creds())).split()
        self.browser = browser
        self.delay = 10
        # self.url = url

    # def open(self):
    #     self.browser.get(self.url)