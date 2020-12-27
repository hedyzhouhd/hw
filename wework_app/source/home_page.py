from appium.webdriver.common.mobileby import MobileBy

from wework_app.source.base_page import BasePage
from wework_app.source.contact_page import ContactPage
from wework_app.source.work_bench_page import WorkBenchPage


class HomePage(BasePage):

    def goto_work_bench(self):
        """
           从首页跳转进入工作台页面
           """
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        return WorkBenchPage(self.driver)

    def goto_contact(self):
        """
        首页点击跳转通讯录页面
        :return:
        """
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']").click()
        return ContactPage(self.driver)
