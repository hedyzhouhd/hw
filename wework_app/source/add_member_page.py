from appium.webdriver.common.mobileby import MobileBy
from wework_app.source.base_page import BasePage


class AddMemberPage(BasePage):
    def add_manual(self):
        """
        手动添加成员
        :return:
        """
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys("test01")
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//*[@text='男']").click()
        # 等待弹窗显示
        self.wait_for(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']", 10)
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys("13418157171")
        self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/..//*[@text='选填']").send_keys(
            "13418157171@139.com")
        self.driver.find_element_by_xpath("//*[contains(@text,'地址')]/..//*[@text='选填']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/js").send_keys("广州市天河区")
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
