import requests


class TokenLogin:
    def get_token(self):
        params = {
            'corpid': 'ww0f805e2a01e56c23',
            'corpsecret': 'c_-dAfij4Ub0lC2r4zBG8dFUsAbR7ctKPRnIIfp20rA'
        }
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params=params
        )
        return r

    def get_token2(self):
        params = {
            'corpid': 'ww0f805e2a01e56c23',
            'corpsecret': 'c_-dAfij4Ub0lC2r4zBG8dFUsAbR7ctKPRnIIfp20rA'
        }
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params=params
        )
        return r.json()['access_token']