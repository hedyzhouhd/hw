from wework_api.api.token import TokenLogin


class TestToken:
    def test_get_token(self):
        r = TokenLogin().get_token()
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_get_token2(self):
        r = TokenLogin().get_token2()
        print(r)
