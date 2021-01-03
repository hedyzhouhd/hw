from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.source.login_page import LoginPage
from wework.source.main_page import MainPage
import pytest


class TestContact:
    def setup(self):
        self.main_page = LoginPage().scan_login()

    def test_get_members(self):
        """
        1.进入首页--点击通讯录跳转通讯录页面--获取成员列表
        :return:
        """
        print(self.main_page.goto_contacts().get_member_list())
        print("hello")

    @pytest.mark.parametrize('phones', [['13411111116', '13411111114']])
    def test_del_members(self, phones):
        member_list_before = self.main_page.goto_contacts().get_member_list()
        tip_locator = (By.ID, "js_tips")
        contact_page = self.main_page.goto_contacts().del_members(phones)
        WebDriverWait(self.main_page.driver, 10).until(expected_conditions.invisibility_of_element(tip_locator))
        # tip_text = self.main_page.driver.find_element(By.ID, "js_tips").text
        tip_text = self.main_page.driver.execute_script("el = document.getElementById('js_tips');return el.textContent")
        member_list_after = contact_page.get_member_list()
        print("member_list_before=%s,长度=%d" % (member_list_before, len(member_list_before)))
        print("member_list_after=%s,长度=%d" % (member_list_after, len(member_list_after)))
        print("tip_text=%s" % tip_text)
        pytest.assume(len(member_list_before)-len(phones) == len(member_list_after))
        pytest.assume(tip_text == "删除成功")
