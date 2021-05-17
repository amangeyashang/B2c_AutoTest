# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/17 11:34'

from selenium import webdriver
import time
import pytest
import os

#商品管理-商品分类
class TestCase(object):
    #定义登录方法
    def login(self,user,pwd):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()#窗口最大化
        self.driver.get("http://192.168.1.112:10010/ui") #卖家端登录域名
        self.driver.find_element_by_id("login-user").send_keys(user)
        self.driver.find_element_by_id("login-password").send_keys(pwd)
        self.driver.find_element_by_id("login-btn").click()
        time.sleep(3)

    def test_commodity(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[4]').click()#商品分类
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()