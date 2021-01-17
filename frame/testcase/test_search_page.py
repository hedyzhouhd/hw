import os
import signal
import subprocess

from frame.testcase.test_base import TestBase
import logging

logging.basicConfig(level=logging.INFO)


class TestSearchPage(TestBase):
    def test_search(self):
        """关键字驱动用例测试"""
        try:
            logging.info("开始打印日志")
            price = self.home_page.goto_search_page().search('alibaba')
            print(price)
            assert float(price) > 200
        except Exception as e:
            logging.info("异常情况：" + str(e))
        finally:
            logging.info("结束打印日志")

    def test_search1(self, record_video):
        price = self.home_page.goto_search_page().search1('alibaba')
        print(price)
        assert float(price) > 200

    def test_record(self):
        cmd = 'scrcpy --record file.mp4'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(p)
        price = self.home_page.goto_search_page().search1('alibaba')
        print(price)
        os.kill(p.pid, signal.CTRL_C_EVENT)
