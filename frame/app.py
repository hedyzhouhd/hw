from appium import webdriver

from frame.base_page import BasePage
from frame.page.home_page import HomePage


class App(BasePage):
    def __init__(self, driver=None):
        self.driver = driver
        if self.driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['automationName'] = 'UiAutomator2'  # 抓取toast信息
            caps['platformVersion'] = '6.0.1'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = ' com.xueqiu.android'
            caps['appActivity'] = '.common.MainActivity'
            caps['noReset'] = 'true'
            caps['settings[waitForIdleTimeout]'] = 0
            caps['unicodeKeyboard'] = 'true'
            caps['resetKeyboard'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(5)

    def goto_home_page(self):
        """
        :return: 跳转app主页面
        """
        return HomePage(self.driver)
