from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.source.add_member_page import AddMemberPage
from wework.source.base_page import BasePage
from selenium.webdriver.common.by import By

from wework.source.contact_page import ContactPage


class MainPage(BasePage):
    def goto_add_member(self):
        el = self.driver.find_element(By.CLASS_NAME, "ww_indexImg_AddMember")
        locate = (By.CLASS_NAME, "ww_indexImg_AddMember")
        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(locate), message="")
        el.click()
        return AddMemberPage(self.driver)

    def goto_contacts(self):
        """
        跳转通讯录页面
        """
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        # return ContactPage(self.driver)
