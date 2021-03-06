from appium.webdriver.common.mobileby import MobileBy

from frame.base_page import BasePage
from frame.page.quotation_page import QuotationPage
from frame.page.search_page import SearchPage


class HomePage(BasePage):
    def goto_quotation_page(self):
        """
        跳转行情页面
        :return:
        """
        # 制造弹窗测试黑名单处理
        self.find_and_click((MobileBy.ID, "com.xueqiu.android:id/post_status"))
        quotation_locator = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']")
        el = self.find(quotation_locator)
        el.click()
        return QuotationPage(self.driver)

    def goto_market_page(self):
        """
        使用关键字驱动方式跳转行情页
        :return:
        """
    def goto_search_page(self):
        self.find_and_click(MobileBy.ID, 'com.xueqiu.android:id/tv_search')
        return SearchPage(self.driver)
