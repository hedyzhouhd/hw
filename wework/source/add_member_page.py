from selenium.webdriver.common.by import By

from wework.source.base_page import BasePage
from selenium import webdriver
from wework.source.contact_page import ContactPage


class AddMemberPage(BasePage):
    _name_locator = (By.ID, 'username')
    _acctid_locator = (By.ID, 'memberAdd_acctid')
    _phone_locator = (By.CSS_SELECTOR, '.ww_telInput_mainNumber')
    _save_locator = (By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self, name, acct_id, phone):
        """成功添加成员
        """
        self.driver.find_element(*self._name_locator).send_keys(name)
        self.driver.find_element(*self._acctid_locator).send_keys(acct_id)
        self.driver.find_element(*self._phone_locator).send_keys(phone)
        self.driver.find_element(*self._save_locator).click()
        return ContactPage(self.driver)

    def add_member_fail(self, name, acct_id, phone, email):
        """添加成员失败
        """
        self.driver.find_element(*self._name_locator).send_keys(name)
        self.driver.find_element(*self._acctid_locator).send_keys(acct_id)
        self.driver.find_element(*self._phone_locator).send_keys(phone)
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(email)
        self.driver.find_element(*self._save_locator).click()
        els = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = []
        for i in range(len(els)):
            error_list.append(els[i].text)
        return error_list
