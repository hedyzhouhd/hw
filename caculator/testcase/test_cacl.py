"""
测试Calcalutor类中的方法
参数化方式实现
"""
from caculator.source.cacl import Calculator
import pytest


class TestCalculator:
    def setup_method(self):
        self.cacl = Calculator()
        print("开始计算")

    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect",
                             [(1, 2, 3), (4.0, 5.9, 9.9), ('s', 5, '错误参数'), (-9, 1, -8)],
                             ids=['int', 'float', 'illegal', 'minus'])
    def test_add(self, a, b, expect):
        assert expect == self.cacl.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [[1, 2, -1], [9.0, 5.9, 3.1], ['s', 5, '错误参数'], [-9, 1, -10]],
                             ids=['int', 'float', 'illegal', 'minus'])
    def test_sub(self, a, b, expect):
        assert expect == self.cacl.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(1, 2, -1), (9.0, 5.9, 3.1), ('s', 5, '错误参数'), (-9, 1, -10)],
                             ids=['int', 'float', 'illegal', 'minus'])
    def test_mul(self, a, b, expect):
        assert expect == self.cacl.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(1, 2, 0.5), (10, 3, 3.1), ('s', 5, '错误参数'), (-9, -1, 10), (4, 0, '被除数不能为0')],
                             ids=['int', 'float', 'illegal', 'minus', 'zero'])
    def test_div(self, a, b, expect):
        assert expect == self.cacl.div(a, b)

    @pytest.mark.parametrize('a', [1, 2, 3])
    @pytest.mark.parametrize('b', [4, 5, 6])
    def test_combine(self, a, b):
        print("a=%s,b=%s" % (a, b))
