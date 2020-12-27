from appium.webdriver.common.mobileby import MobileBy

from wework_app.source.base_page import BasePage
from wework_app.source.clock_page import ClockPage


class WorkBenchPage(BasePage):
    """
    工作台页面跳转进入打卡页面
    """
    def goto_clock_page(self):
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        return ClockPage(self.driver)