import pytest

from wework.source.main_page import MainPage


class TestMember:
    def setup_class(self):
        self.main_page = MainPage()
    def test_add_memeber(self):
        """
        1.进入首页 2.点击添加成员 3.添加成功
        :return:
        """
        self.main_page.goto_add_member().add_member()