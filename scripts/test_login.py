import os
import sys

sys.path.append(os.getcwd())

from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin():
    def setup_class(self):
        # 实例化PageLogin
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        # 关闭驱动对象
        self.login.driver.quit()

    def test_login(self, message='！'):
        # 点击登陆
        self.login.page_click_login_btn()
        # 获取toast消息
        toast_msg = self.login.page_get_toast(message)

        print("获取的toast消息为：", toast_msg)
