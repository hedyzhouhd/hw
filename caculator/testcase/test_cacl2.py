"""
测试Calcalutor类中的方法
通过yaml文件实现参数化
"""
import os
import yaml
from caculator.source.cacl import Calculator
import pytest


def get_yml_data():
    data_path = os.path.abspath(os.path.join(os.getcwd(), "..", 'data/cacl.yml'))
    data = yaml.safe_load(open(data_path, encoding='utf-8'))
    return data
    # print(data)
    # print(data['add']['values'])


def test_path():
    print(os.getcwd())
    print(os.path.abspath('..'))
    print(os.path.abspath(os.path.join(os.getcwd(), "..", 'data/cookies.yml')))


class TestCalculator:
    def setup_method(self):
        self.cacl = Calculator()
        self.data = get_yml_data()
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['add']['values'],
                             ids=get_yml_data()['add']['ids'])
    def test_add(self, a, b, expect):
        assert expect == self.cacl.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['sub']['values'],
                             ids=get_yml_data()['sub']['ids'])
    def test_sub(self, a, b, expect):
        assert expect == self.cacl.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['mul']['values'],
                             ids=get_yml_data()['mul']['ids'])
    def test_mul(self, a, b, expect):
        assert expect == self.cacl.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['div']['values'],
                             ids=get_yml_data()['div']['ids'])
    def test_div(self, a, b, expect):
        assert expect == self.cacl.div(a, b)
