from wework.source.base_page import BasePage
from wework.source.contact_page import ContactPage


class ImportMbrPage(BasePage):
    def import_member(self):
        """
        文件导入成员信息
        :return: 返回通讯页面
        """
        return ContactPage(self.driver)
