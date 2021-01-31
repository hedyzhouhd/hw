import requests
import json

from wework_api.api.base import Base


class Member(Base):
    def create_member(self, data):
        """
        ToDO:1.中文编码问题  --解决部门问题2后问题1就没有出现了
             2.创建成功，但是有warnings:{"errcode":0,"errmsg":"created. Warning: wrong json format. "}--部门是列表类型
        :param data:
        :return:
        """
        r = self.s.post(
            url="".join([self.host, '/cgi-bin/user/create']),
            headers={
                'Content-Type': 'application/json; charset=UTF-8'
            },
            data=json.dumps(data)
        )
        return r.json()

    def update_member(self, data: dict):
        r = self.s.post(
            url="".join([self.host, '/cgi-bin/user/update']),
            data=json.dumps(data)
        )
        return r.json()

    def get_member(self, userid):
        params = {
            'userid': userid
        }
        r = self.s.get(
            url="".join([self.host, '/cgi-bin/user/get']),
            params=params
        )
        return r.json()

    def delete_member(self, userid):
        params = {
            'userid': userid
        }
        r = self.s.get(
            url="".join([self.host, '/cgi-bin/user/delete']),
            params=params
        )
        return r.json()
