import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from frame.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(MobileBy.ID, 'com.xueqiu.android:id/iv_close')]

    @handle_black
    def find(self, by, locator):
        """
        封装查找元素方法
        :param locator:
        :return: 查找的元素
        """
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        """
        查找到元素并进行点击
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        """
        查找到元素并进行文本输入
        :param by:
        :param locator:
        :param text:
        :return:
        """
        el = self.find(by, locator)
        el.send_keys(text)

    def wait_for(self, by, locator, sec: int):
        def wait_for_el(driver: WebDriver):
            els = driver.find_elements(by, locator)
            return len(els) > 0

        WebDriverWait(self.driver, sec).until(wait_for_el)

    def scroll_find_click(self, text):
        """滑动查找指定元素并进行点击"""
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      f'text("{text}").instance(0));').click()

    def swipe_find_click(self, by, locator):
        """滑动查找指定元素并进行点击"""
        els = self.driver.find_elements(by, locator)
        find_times = 0
        window_rect = self.driver.get_window_rect()
        height = window_rect['height']
        while len(els) == 0 and find_times < 5:
            self.driver.swipe(0, height * (find_times + 1) / 5, 0, height * find_times / 5)
            els = self.driver.find_elements(by, locator)
        els[0].click()

    def load_step(self, yaml_path, *args):
        """
        关键字驱动
        :param yaml_path: 关键字驱动yaml文件路径
        :param args: send方法输入的内容，列表长度与send个数一致
        :return:
        """
        res = []
        data = yaml.safe_load(open(yaml_path, encoding='utf-8'))
        i = 0
        for step in data:
            locator = step.get('locator')
            by = step.get('by')
            action = step.get('action')
            if action == "find_and_click":
                self.find_and_click(by, locator)
            elif action == "find_and_send":
                content = args[i]
                i = i+1
                print(eval(by))
                self.driver.find_element(eval(by), locator).send_keys(content)
            elif action == "text":
                tmp_text = self.driver.find_element(by, locator).text
                res.append(tmp_text)
        return res
