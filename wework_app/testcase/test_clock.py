from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from wework_app.source.home_page import HomePage


class TestClock:
    def setup(self):
        self.work_bench = HomePage().goto_work_bench()

    def teardown(self):
        self.work_bench.driver.quit()

    def test_clock(self):
        """
        测试使用android原生功能滑动至打卡处
        1.进入企业微信首页，点击工作台-点击打卡--点击外出打卡

        """
        clock = self.work_bench.goto_clock_page()
        clock.out_clock()
        # print(self.driver.page_source)
        WebDriverWait(clock.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert '外出打卡成功' in clock.driver.page_source

    def test_clock2(self):
        """
        测试使用swip方法滑动至打卡处
        1.进入企业微信首页，点击工作台-点击打卡--点击外出打卡
        """
        clock = self.work_bench.goto_clock_page2()
        clock.out_clock()
        self.work_bench.wait_for(MobileBy.XPATH, "//*[@text='外出打卡成功']", 10)
        assert '外出打卡成功' in clock.driver.page_source
