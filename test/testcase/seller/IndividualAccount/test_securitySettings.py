# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/21 11:19'

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

    def test_securitySettings_changePassword(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[10]/div/span').click()#个人账户
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[10]/ul/li').click()#安全设置
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="oldPassword"]').send_keys("123456")#当前密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="newPassword"]').send_keys("123456")#设置新密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="newPasswordAgain"]').send_keys("123456")#确认新密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="update-password"]/div[2]/div/form/table/tbody/tr[5]/td/button').click()#确认
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()