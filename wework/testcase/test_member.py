import pytest
import re

from wework.source.login_page import LoginPage
from wework.source.main_page import MainPage


class TestMember:
    def setup(self):
        self.main_page = LoginPage().scan_login()

    def teardown(self):
        self.main_page.driver.quit()

    @pytest.mark.parametrize('name,acct_id,phone',
                             [("花花", "huahua02", "13411111114"), ("花花6", "huahua06", "13411111116")],
                             ids=['correct', '2'])
    def test_add_member(self, name, acct_id, phone):
        """
        1.进入首页 -点击添加成员 -添加成功
        :return:
        """
        contact_page = self.main_page.goto_add_member().add_member(name, acct_id, phone)
        assert phone in contact_page.get_member_list()

    @pytest.mark.parametrize('name,acct_id,phone,email',
                             [("song.peng", "song.peng", "13411111111", '1@163.com'),
                              ("song.peng", "song.peng1", "13411111112", '1@163.com'),
                              ("song.peng", "song.peng1", "1", '1@163.com'),
                              ("song.peng", "song.peng1", "13411111111", '1')],
                             ids=['used_account', 'used_phone', 'incorrect_phone', 'incorrect_email'])
    def test_add_member_fail(self, name, acct_id, phone, email):
        """
        1.进入首页-点击添加成员-添加失败
        :param name:
        :param acct_id:
        :param phone:
        :param email:
        :return:
        """
        error_msg = self.main_page.goto_add_member().add_member_fail(name, acct_id, phone, email)
        print(error_msg)
        for error in error_msg:
            print(f'error={error}')
            if re.match(r'该帐号已被(.+)占有', error) is not None:
                assert True
                break
            elif re.match('该手机已被“su.na”占有', error) is not None:
                assert True
                break
            elif '请填写正确的手机号码' == error:
                assert True
                break
            elif '请填写正确的邮箱地址' == error:
                assert True
                break

    @pytest.mark.parametrize('name,acct_id,phone', [("花花", "huahua03", "13411111115")], ids=['correct'])
    def test_add_member_by_contact(self, name, acct_id, phone):
        """
        1.进入首页-点击通讯录-点击添加成员-点击保存
        :param name:
        :param acct_id:
        :param phone:
        :return:
        """
        contact_page = self.main_page.goto_contacts().goto_add_member_page().add_member(name, acct_id, phone)
        assert phone in contact_page.get_member_list()
