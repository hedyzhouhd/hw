from selenium.webdriver.common.by import By

from wework.source.base_page import BasePage
from selenium import webdriver


class AddMemberPage(BasePage):

    def add_member(self):
        self.driver.find_element(By.ID, 'username').send_keys("花花01")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("huahua01")
        self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_mainNumber').send_keys("13411111111")
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return