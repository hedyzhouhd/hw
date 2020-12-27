from wework_app.source.home_page import HomePage


class TestAddMember:
    def setup(self):
        self.add_member_page = HomePage().goto_contact().goto_add_member_page()
        pass

    def teardown(self):
        pass

    def test_add_manual(self):
        self.add_member_page.add_manual()