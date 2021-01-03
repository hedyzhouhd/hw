from wework.source.base_page import BasePage
from wework.source.main_page import MainPage


class LoginPage(BasePage):
    def scan_login(self):
        """
        扫码登录功能
        :return: 登录成功跳转主页面main_page
        """
        self.get_cookies()
        self.set_cookies()
        return MainPage(self.driver)
