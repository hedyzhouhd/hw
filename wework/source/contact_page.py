from selenium.webdriver.common.by import By
from wework.source.add_depart_page import AddDepartPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.source.base_page import BasePage
import time


class ContactPage(BasePage):

    def goto_add_member_page(self):
        """
        点击添加成员。跳转添加成员页面
        :return:
        """
        from wework.source.add_member_page import AddMemberPage
        member_locator = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(member_locator))
        # self.driver.find_element(*member_locator).click()
        self.wait_and_click(member_locator, 10)
        return AddMemberPage(self.driver)

    def get_member_list(self):
        """获取成员列表
        :return:
        """
        # member_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
        phone_locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(phone_locator))
        phone_list = self.driver.find_elements(*phone_locator)
        members_phone = []
        for phone in phone_list:
            members_phone.append(phone.text)
        return members_phone

    def del_members(self, phones: list):
        """
        根据手机号码删除成员:勾选所有需要删除手机号码所在行，点击删除
        :param phones: 手机号码列表
        :return: 返回通讯录页（当前页）
        """
        time.sleep(2)
        for phone in phones:
            # phone_locator = (By.CSS_SELECTOR, f'{phone}')
            phone_locator = (By.XPATH, f"//*[@title='{phone}']/preceding-sibling::*[last()]")
            self.wait_and_click(phone_locator)
        self.driver.find_element(By.CSS_SELECTOR, '.js_delete').click()
        self.driver.find_element(By.LINK_TEXT, "确认").click()
        return ContactPage(self.driver)

    def goto_add_sub_depart(self):
        """
        1.点击添加子部门-跳转新增部门页面
        :return: 跳转新增部门页面
        """
        depart_locator = (By.CSS_SELECTOR, ".js_add_sub_party")
        self.wait_and_click(depart_locator, 10)
        return AddDepartPage(self.driver)

    def goto_add_depart(self):
        """
        1.点击+图标--点击添加部门
        :return:跳转添加部门页
        """
        locator = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
        # self.driver.find_element(*locator).click()
        self.wait_and_click(locator)
        self.wait_and_click((By.LINK_TEXT, '添加部门'))
        # self.driver.find_element(By.LINK_TEXT, '添加部门').click()
        return AddDepartPage(self.driver)

    def get_depart_list(self):
        """
        获取所有的部门
        :return: 返回部门名称列表
        """
        depart_locator = (By.CSS_SELECTOR, ".jstree-container-ul a")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(depart_locator))
        depart_elements = self.driver.find_elements(*depart_locator)
        depart_list = []
        for depart in depart_elements:
            depart_list.append(depart.text)
        return depart_list

    def goto_import_member(self):
        """
        点击批量导入/导出-文件导入
        :return:跳转导入页面
        """