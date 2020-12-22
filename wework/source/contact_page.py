from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.source.base_page import BasePage
from selenium import webdriver


class ContactPage(BasePage):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def goto_add_member_page(self):
        pass
        # WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable())

    def get_member_list(self):
        """获取成员列表
        :return:
        """
        pass