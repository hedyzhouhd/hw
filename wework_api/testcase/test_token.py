from wework_api.api.base import Base


class TestToken:
    def test_get_token(self):
        r = Base().get_token()
        print(r)
        assert r['errcode'] == 0

    def test_get_token2(self):
        r = Base().get_token2()
        print(r)
