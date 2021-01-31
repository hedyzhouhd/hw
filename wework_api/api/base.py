import requests


class Base:
    def __init__(self):
        self.corp_id = 'ww0f805e2a01e56c23'
        self.corp_secret = 'c_-dAfij4Ub0lC2r4zBG8dFUsAbR7ctKPRnIIfp20rA'
        self.host = r'https://qyapi.weixin.qq.com'
        self.s = requests.Session()
        self.s.params['access_token'] = self.get_token().get('access_token')

    def get_token(self, corp_id=None, corp_secret=None):
        if corp_id is None:
            corp_id = self.corp_id
        if corp_secret is None:
            corp_secret = self.corp_secret
        params = {
            'corpid': corp_id,
            'corpsecret': corp_secret
        }
        r = requests.get(
            url="".join([self.host, '/cgi-bin/gettoken']),
            params=params
        )
        return r.json()

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
