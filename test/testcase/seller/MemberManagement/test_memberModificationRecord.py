# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/21 10:53'

from selenium import webdriver
import time
import pytest
import os

#会员管理-会员修改记录
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

    def test_memberModificationRecord_modify(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[6]/div/span').click()#会员管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[6]/ul/li[3]').click()#会员修改记录
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/input').click()#是否修改
        time.sleep(1)
        option = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul')
        option.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[3]/button').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_memberModificationRecord_membershipNumber(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[6]/div/span').click()#会员管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[6]/ul/li[3]').click()#会员修改记录
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[2]/div[2]/div/input').send_keys("000006")#会员号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[3]/button').click()#搜索
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()
