# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/6/25 15:34'
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')

class LoginPage(WebPage):
    """登录类"""

    def input_account(self,content):
        """输入账号"""
        self.input_text(login['账号'],txt=content)
        sleep()

    def input_password(self,content):
        """输入密码"""
        self.input_text(login['密码'],txt=content)
        sleep()

    def click_login(self):
        """点击登录"""
        self.is_click(login['登录按钮'])
