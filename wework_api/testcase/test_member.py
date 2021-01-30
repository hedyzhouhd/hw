import json

import pytest

from wework_api.api.member import Member

data_dict = {
    "userid": "zhangsan",
    "name": "张三",
    "alias": "jackzhang",
    "mobile": "+86 13800000000",
    "department": '3'
}


class TestMember:
    def setup_class(self):
        self.member = Member()

    @pytest.mark.parametrize('data', [data_dict])
    def test_create_member(self, data):
        r = self.member.create_member(data)
        print(r.raw)
        assert r.json()['errcode'] == 0

    def test_get_member(self):
        r = self.member.get_member('huahua06')
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_delete_member(self):
        r = self.member.delete_member('zhangsan')
        print(r.json())
        assert r.json()['errcode'] == 0