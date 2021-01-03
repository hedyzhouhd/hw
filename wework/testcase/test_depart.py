import pytest
from selenium.webdriver.common.by import By

from wework.source.login_page import LoginPage
from wework.source.main_page import MainPage


class TestDepart:
    def setup(self):
        self.contact_page = LoginPage().scan_login().goto_contacts()

    @pytest.mark.parametrize('depart_name, parent_depart_name', [('test022', 'test02')])
    def test_add_depart(self, depart_name, parent_depart_name):
        self.contact_page.goto_add_depart().add_department(depart_name, parent_depart_name)
        assert "新建部门成功" == self.contact_page.driver.find_element(By.CSS_SELECTOR, '#js_tips').text
        assert depart_name in self.contact_page.get_depart_list()

    def test_get_depart_list(self):
        print(self.contact_page.get_depart_list())
