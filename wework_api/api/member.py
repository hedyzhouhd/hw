import requests
import json

from wework_api.api.token import TokenLogin


class Member:
    def __init__(self):
        self.access_token = TokenLogin().get_token2()

    def create_member(self, data):
        r = requests.post(
            url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}',
            data={
                "userid": "zhangsan",
                "name": "张三",
                "alias": "jackzhang",
                "mobile": "+86 13800000000",
                "department": '3'
            }
        )
        return r

    def get_member(self, userid):
        params = {
            'access_token': self.access_token,
            'userid': userid
        }
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/user/get',
            params=params
        )
        return r

    def delete_member(self, userid):
        params = {
            'access_token': self.access_token,
            'userid': userid
        }
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            params=params
        )
        return r
