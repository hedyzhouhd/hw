from selenium.webdriver.common.by import By

from wework.source.base_page import BasePage
from wework.source.login_page import LoginPage
from wework.source.register_page import RegisterPage


class IndexPage(BasePage):
    def goto_login_page(self):
        """
        点击企业登录
        :return:跳转登录页面
        """
        login_locator = (By.CSS_SELECTOR, ".index_top_operation_loginBtn")
        self.wait_and_click(login_locator)
        return LoginPage(self.driver)

    def goto_register_page(self):
        self.driver.get("https://work.weixin.qq.com/")
        register_locator = (By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn")
        self.wait_and_click(register_locator)
        return RegisterPage(self.driver)
