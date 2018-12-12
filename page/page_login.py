import page
from base.base import Base


class PageLogin(Base):
    # 点击登陆
    def page_click_login_btn(self):
        self.base_click_element(page.login_btn)

    # 获取toast消息
    def page_get_toast(self, message):
        return self.base_get_toast_info(message)
