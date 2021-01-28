import os
import signal
import subprocess
import traceback

import allure
import pytest
import time

from frame.testcase.test_base import TestBase
import logging

logging.basicConfig(level=logging.INFO)


class TestSearchPage(TestBase):
    @pytest.mark.skip
    def test_search(self):
        """关键字驱动用例测试"""
        try:
            logging.info("开始打印日志")
            price = self.home_page.goto_search_page().search('alibaba')
            print(price)
            assert float(price) > 200
        except Exception as e:
            image_path = "search.png"
            self.home_page.driver.save_screenshot(image_path)
            with open(image_path, 'rb') as f:
                data = f.read()
            allure.attach(data, attachment_type=allure.attachment_type.PNG)
            logging.info("异常情况：" + traceback.format_exc())
        finally:
            logging.info("结束打印日志")

    def test_search1(self, record_video):
        mp4 = record_video
        time.sleep(5)
        price = self.home_page.goto_search_page().search1('alibaba')
        print(price)
        with open(mp4, 'rb') as f:
            data = f.read()
        allure.attach(data, attachment_type=allure.attachment_type.MP4)
        assert float(price) > 200

    @pytest.mark.skip
    def test_record(self):
        cmd = 'scrcpy --record file.mp4'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(p)
        price = self.home_page.goto_search_page().search1('alibaba')
        print(price)
        os.kill(p.pid, signal.CTRL_C_EVENT)
