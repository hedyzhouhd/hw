from appium.webdriver.common.mobileby import MobileBy

from wework_app.source.base_page import BasePage
from wework_app.source.work_bench_page import WorkBenchPage


class HomePage(BasePage):
    """
    从首页跳转进入工作台页面
    """
    def goto_work_bench(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        return WorkBenchPage(self.driver)
