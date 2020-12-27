from appium.webdriver.common.mobileby import MobileBy

from wework_app.source.add_member_manual import AddMemberManual
from wework_app.source.base_page2 import BasePage2


class AddMbrPage(BasePage2):
    def goto_add_manual(self):
        """
        点击手动输入添加成员
        :return:跳转手动添加成员页面
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return AddMemberManual(self.driver)
