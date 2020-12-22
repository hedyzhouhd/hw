"""
测试Calcalutor类中的方法
1)通过yaml文件实现参数化
2)使用fixture替换setup和teardown
3)将fixture方法放在conftest.py里面，设置scope=module
4)控制用例的执行顺序-乘加除减
5)test_add设置失败重跑2次
6)结合allure生成测试结果报告
"""
import os
import yaml
import pytest


def get_yml_data():
    data_path = os.path.abspath(os.path.join(os.getcwd(), "..", 'data/cacl.yml'))
    data = yaml.safe_load(open(data_path, encoding='utf-8'))
    return data


class TestCalculator:
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['add']['values'],
                             ids=get_yml_data()['add']['ids'])
    def test_add(self, a, b, expect, fixture_cacl):
        res = fixture_cacl.add(a, b)
        assert expect == res

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['sub']['values'],
                             ids=get_yml_data()['sub']['ids'])
    def test_sub(self, a, b, expect, fixture_cacl):
        assert expect == fixture_cacl.sub(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['mul']['values'],
                             ids=get_yml_data()['mul']['ids'])
    def test_mul(self, a, b, expect, fixture_cacl):
        assert expect == fixture_cacl.mul(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect",
                             get_yml_data()['div']['values'],
                             ids=get_yml_data()['div']['ids'])
    def test_div(self, a, b, expect, fixture_cacl):
        assert expect == fixture_cacl.div(a, b)
