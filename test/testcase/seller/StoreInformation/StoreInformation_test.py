# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/13 11:00'

from selenium import webdriver
import time
import pytest
import os

#店铺信息-店铺基础数据
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

    #测试用例 B2C_seller_StoreInformation
    def test_storeInformation_success(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[1]/div/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[1]/ul/li').click()
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()