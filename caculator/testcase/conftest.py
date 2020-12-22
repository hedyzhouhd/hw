import os

import pytest
import yaml

from caculator.source.cacl import Calculator


@pytest.fixture(scope="module")
def fixture_cacl():
    cacl = Calculator()
    print("开始计算")
    yield cacl
    print("计算结束")


@pytest.fixture(scope="module", params=['cacl.yml'])
def fixture_data(request):
    print("开始使用yml")
    data_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'data/', request.param))
    data = yaml.safe_load(open(data_path, encoding='utf-8'))
    yield data
    print("结束使用yml")