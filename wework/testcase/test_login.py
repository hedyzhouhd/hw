import yaml

from wework.source.wework_login import WeWorkLogin


class TestLogin:
    def test_login(self):
        obj = WeWorkLogin()
        print(obj.file_path)
        obj.login()
        obj.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")


