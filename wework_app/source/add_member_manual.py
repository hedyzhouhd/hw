from appium.webdriver.common.mobileby import MobileBy
from wework_app.source.base_page2 import BasePage2


class AddMemberManual(BasePage2):

    def add_manual(self, name, phone, email, address):
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//*[@text='男']").click()
        # 等待弹窗显示
        self.wait_for(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']", 10)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(phone)
        self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/..//*[@text='选填']").send_keys(email)
        self.driver.find_element_by_xpath("//*[contains(@text,'地址')]/..//*[@text='选填']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/js").send_keys(address)
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

    def add_manual_fail(self):
        """
              1)手机号码重复：手机已存在于通讯录，无法添加
              2）邮箱已存在于通讯录，无法添加
              :return:
        """

        pass
