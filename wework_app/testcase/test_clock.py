from selenium.webdriver.support.wait import WebDriverWait
from wework_app.source.home_page import HomePage


class TestClock:
    def setup(self):
        self.clock = HomePage().goto_work_bench().goto_clock_page()

    def teardown(self):
        self.clock.driver.quit()

    def test_clock(self):
        """
        1.进入企业微信首页，点击工作台-点击打卡--点击外出打卡
        """
        self.clock.out_clock()
        # print(self.driver.page_source)
        WebDriverWait(self.clock.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert '外出打卡成功' in self.clock.driver.page_source
