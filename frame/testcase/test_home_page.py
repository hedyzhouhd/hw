from frame.testcase.test_base import TestBase


class TestMainPage(TestBase):
    def test_goto_quotation_page(self):
        self.home_page.goto_quotation_page()
