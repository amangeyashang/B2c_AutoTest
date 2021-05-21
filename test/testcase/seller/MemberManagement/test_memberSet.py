# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/21 10:27'

from selenium import webdriver
import time
import pytest
import os
import random

#会员管理-会员设置
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

    def test_memberSet_membershipRightsSettings(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[6]/div/span').click()#会员管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[6]/ul/li[2]').click()#会员设置
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[5]/div/button/span').click()#会员权益设置
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/form/div[2]/div/ul/li[2]/label/span/span').click()#会员价
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/form/div[3]/div/div/input').clear()#推荐直返
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/form/div[3]/div/div/input').send_keys(random.randint(0,100))#推荐直返
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/form/div[4]/div/div[2]/div/input').clear()#分润
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/form/div[4]/div/div[2]/div/input').send_keys(random.randint(0,100))#分润
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/form/div[5]/div/div/textarea').send_keys("测试测试")#说明
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="basic-data"]/div[2]/div/div/button[2]/span').click()#提交
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()