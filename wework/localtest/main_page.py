from selenium import webdriver
from selenium.webdriver.common.by import By

from wework.localtest.base_page import BasePage1


class MainPage(BasePage1):
    def goto_contact(self):
        """跳转到通讯录页面
        :return:
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def back_main(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()