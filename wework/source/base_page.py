import os

import yaml
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            options = webdriver.ChromeOptions()
            options.debugger_address = '127.0.0.1:9227'
            self.driver = webdriver.Chrome(options=options)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.file_path = os.path.abspath(
                os.path.join(os.getcwd(), "..", "..", 'wework/data/wework_login_cookies.yml'))
            self.get_cookies()
            self.set_cookies()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        # print(cookies)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            yaml.dump(cookies, f)

    def set_cookies(self):
        cookies = yaml.safe_load(open(self.file_path, encoding='utf-8'))
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
