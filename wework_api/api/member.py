import requests
import json

from wework_api.api.token import TokenLogin


class Member:
    def __init__(self):
        self.access_token = TokenLogin().get_token2()

    def create_member(self, data):
        """
        ToDO:1.中文编码问题  2.创建成功，但是有warnings:{"errcode":0,"errmsg":"created. Warning: wrong json format. "}
        :param data:
        :return:
        """
        r = requests.post(
            url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}',
            headers={
                'Content-Type': 'application/json; charset=UTF-8'
            },
            data=json.dumps(data)
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

