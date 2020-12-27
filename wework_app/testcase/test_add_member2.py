from wework_app.source.app import App
from wework_app.source.home_page import HomePage


class TestAddMember:
    def setup(self):
        """
        启动app-进入首页-点击通讯录-点击添加成员-点击手动添加成员
        :return: 进入手动添加成员页面
        """
        self.add_member_page = App().goto_home_page().goto_contact().goto_add_mbr_page()
        pass

    def teardown(self):
        pass

    def test_add_manual(self):
        """点击手动添加-进入手动添加成员页面-添加成员"""
        self.add_member_page.goto_add_manual().add_member()
