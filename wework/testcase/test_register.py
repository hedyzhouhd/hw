from wework.source.index_page import IndexPage
from wework.source.register_page import RegisterPage


class TestRegister:
    def test_register(self):
        IndexPage().goto_register_page().register()