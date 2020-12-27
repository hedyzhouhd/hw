from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""企业微信app项目测试"""


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0.1'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.LaunchSplashActivity'
            caps['noReset'] = 'true'
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def wait_for(self, by, locator, sec: int):
        def wait_for_el(driver: WebDriver):
            els = driver.find_elements(by, locator)
            return len(els) > 0

        WebDriverWait(self.driver, sec).until(wait_for_el)
