from wework.localtest.main_page import MainPage
from wework.source.login_page import LoginPage


class TestMainPage:
    def setup_class(self):
        self.main_page = LoginPage().scan_login()

    def test_goto_contacts(self):
        self.main_page.goto_contacts()
