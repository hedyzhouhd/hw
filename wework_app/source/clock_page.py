from appium.webdriver.common.mobileby import MobileBy

from wework_app.source.base_page import BasePage


class ClockPage(BasePage):

    def out_clock(self):
        """
        外出打卡功能
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()