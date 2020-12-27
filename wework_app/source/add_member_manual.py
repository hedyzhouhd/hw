from appium.webdriver.common.mobileby import MobileBy
from wework_app.source.base_page2 import BasePage2


class AddMemberManual(BasePage2):
    def add_member(self):
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']", "test01")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        # 等待弹窗显示
        self.wait_for(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']", 10)
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']", "13418157171")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'邮箱')]/..//*[@text='选填']", "13418157171@139.com")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'地址')]/..//*[@text='选填']")
        self.find_and_send(MobileBy.ID, "com.tencent.wework:id/js", "广州市天河区")
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
