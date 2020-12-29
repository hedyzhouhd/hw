from appium.webdriver.common.mobileby import MobileBy

from wework_app.source.add_mbr_page import AddMbrPage
from wework_app.source.add_member_page import AddMemberPage
from wework_app.source.base_page import BasePage
from wework_app.source.base_page2 import BasePage2


class ContactPage(BasePage2):
    def goto_add_member_page(self):
        """
        点击进入添加成员界面
          1）成员列表多时，需要滑动查找添加成员
        :return:
        """
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        return AddMemberPage(self.driver)

    def goto_add_mbr_page(self):
        """
        点击添加成员-跳转进入添加成员页面add_mbr_page
        """
        self.scroll_find_click("添加成员")
        return AddMbrPage(self.driver)
