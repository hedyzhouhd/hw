from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.source.base_page import BasePage
import time


class AddDepartPage(BasePage):

    _depart_input_locator = (By.CSS_SELECTOR, ".inputDlg_item input")
    _submit_locator = (By.LINK_TEXT, '确定')

    # def add_sub_department(self, depart_name):
    #     """
    #     新增部门
    #     :return:新增成功后返回通讯录页面
    #     """
    #     from wework.source.contact_page import ContactPage
    #     self.wait_for_visible(self._depart_input_locator)
    #     self.driver.find_element(*self._depart_input_locator).send_keys(depart_name)
    #     self.driver.find_element(*self._submit_locator).click()
    #     return ContactPage(self.driver)

    def add_department(self, depart_name, parent_depart_name):
        """
        左侧菜单+新增部门（没有处理菜单多层级的问题）
        :param depart_name: 新增部门名称
        :param parent_depart_name: 新增部门所属部门
        :return:新增成功后返回通讯录页
        """
        from wework.source.contact_page import ContactPage
        self.driver.find_element(*self._depart_input_locator).send_keys(depart_name)
        self.wait_and_click((By.CLASS_NAME, "js_parent_party_name"))
        parent_locator = (By.XPATH, f"//*[@class='member_tag_dialog_inputDlg']//*[text()='{parent_depart_name}']")
        print(parent_locator)
        # self.wait_and_click(parent_locator)
        el = self.driver.find_element(*parent_locator)
        self.driver.execute_script("arguments[0].click();", el)
        # self.driver.find_element(*self._submit_locator).click()
        # r

        # locator = (By.LINK_TEXT, f'{parent_depart_name}')
        # els = self.driver.find_elements(*locator)
        # print(len(els))
