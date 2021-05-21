# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/18 15:27'

from selenium import webdriver
import time
import pytest
import os

#订单管理-订单列表
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

    def test_orderCrossList_allOrders_exportList(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[2]').click()#订单交叉列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tab-ALL"]').click()#所有订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[2]/div[3]/form/button').click()#导出列表
        time.sleep(3)
        self.driver.close()

    def test_orderCrossList_allOrders_exportCrossList(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[2]').click()#订单交叉列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tab-ALL"]').click()#所有订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[2]/div[4]/form').click()#导出交叉列表
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()