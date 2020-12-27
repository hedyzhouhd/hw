from selenium.webdriver.common.by import By

from wework.source.add_depart_page import AddDepartPage
from wework.source.base_page import BasePage
from wework.source.main_page import MainPage


class ContactPage(BasePage):

    def goto_add_member_page(self):
        pass
        # WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable())

    def goto_add_depart_page(self):
        """
        点击新增菜单，跳转新增部门页面
        :return: 跳转新增部门页面
        """
        return AddDepartPage(self.driver)

    def get_member_list(self):
        """获取成员列表
        :return:
        """
        member_list = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_tr')
        for member in member_list:
            print(member)