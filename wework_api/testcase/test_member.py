import pytest

from wework_api.api.member import Member

data_dict = {
    "userid": "zhangsan",
    "name": "张三",
    "alias": "jackzhang",
    "mobile": "+86 13800000000",
    "department": ['3']
}


class TestMember:
    def setup_class(self):
        self.member = Member()

    @pytest.mark.parametrize('data', [data_dict])
    def test_create_member(self, data):
        r = self.member.create_member(data)
        print(r)
        try:
            member_obj = self.member.get_member(data['userid'])
        finally:
            self.member.delete_member(data['userid'])
        assert r['errcode'] == 0 and member_obj['userid'] == data['userid']

    @pytest.mark.parametrize('tmp', range(20))
    def test_get_member(self, tmp):
        r = self.member.get_member('lisi')
        print("r=%s" % r)
        assert r['errcode'] == 0

    def test_delete_member(self):
        self.member.create_member(data_dict)
        member_obj = self.member.get_member(data_dict['userid'])
        r = self.member.delete_member(member_obj['userid'])
        print(r)
        assert r['errcode'] == 0

    @pytest.mark.parametrize('data', [data_dict])
    def test_update_member(self, data):
        self.member.create_member(data)
        data['name'] = '中国'
        try:
            r = self.member.update_member(data)
            member_obj = self.member.get_member(data['userid'])
        finally:
            self.member.delete_member(data['userid'])
        assert member_obj['name'] == '中国' and r['errcode'] == 0

    @pytest.mark.skip
    def test_delete_member2(self):
        self.member.delete_member('lisi')

    @pytest.mark.skip
    def test_create_member2(self):
        data2 = {
            "userid": "lisi",
            "name": "李四",
            "alias": "lisichen",
            "mobile": "+86 13800000001",
            "department": ['3']
        }
        self.member.create_member(data2)
