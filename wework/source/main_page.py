from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.source.add_member_page import AddMemberPage
from wework.source.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        el = self.driver.find_element(By.CLASS_NAME, "ww_indexImg_AddMember")
        locate = (By.CLASS_NAME, "ww_indexImg_AddMember")
        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(locate), message="")
        el.click()
        return AddMemberPage(self.driver)

    def goto_contacts(self):
        pass


if __name__ == "__main__":
    obj = MainPage()
    obj.goto_add_member()

