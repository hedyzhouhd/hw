from frame.testcase.test_base import TestBase


class TestMainPage(TestBase):
    def test_goto_quotation_page(self):
        self.home_page.goto_quotation_page()

    def test_yaml(self):
        yaml_path = r"../page/home.yaml"
        self.home_page.load_step(yaml_path)
