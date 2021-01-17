import os
import signal

from appium.webdriver.common.mobileby import MobileBy

from frame.base_page import BasePage
from time import sleep


class SearchPage(BasePage):
    def search1(self, keyword):
        text_locator = (MobileBy.ID, 'com.xueqiu.android:id/search_input_text')
        self.find_and_send(*text_locator, keyword)
        # self.driver.press_keycode(66)
        sleep(2)
        # todo:为什么输入框输入信息后，还要点击一下，模糊匹配列表才显示
        self.driver.find_element(*text_locator).click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='09988']").click()
        el = self.driver.find_element(MobileBy.XPATH,
                                      "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        return el.text

    def search(self, keyword):
        """关键字驱动方式实现测试用例"""
        return self.load_step("../page/search.yaml", keyword)
