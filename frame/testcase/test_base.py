from frame.app import App
from time import sleep


class TestBase:

    def setup(self):
        self.home_page = App().goto_home_page()

    def teardown(self):
        sleep(10)
        self.home_page.driver.quit()
