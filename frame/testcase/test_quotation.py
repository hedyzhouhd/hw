from frame.app import App
from time import sleep


class TestQuotationPage:
    def setup(self):
        self.home_page = App().goto_home_page()

    def teardown(self):
        sleep(10)
        self.home_page.driver.quit()

    def test_goto_hot_stock_page(self):
        self.home_page.goto_quotation_page()
