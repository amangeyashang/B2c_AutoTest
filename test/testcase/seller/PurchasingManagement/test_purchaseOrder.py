# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/18 19:05'

from selenium import webdriver
import time
import pytest
import os

#采购管理-采购平台
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

    def test_purchaseOrder_stateScreening(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[2]').click()#采购订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[1]/div[2]/div/div/input').click()#状态
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/button').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchaseOrder_preparedBySearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[2]').click()#采购订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys("测试2")#制单人
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/button').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchaseOrder_creationTimeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[2]').click()#采购订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[3]/div[2]/div/input[1]').click()#创建时间
        time.sleep(1)
        window = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]')
        window.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/button[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/button').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchaseOrder_seeDetails(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[2]').click()#采购订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/a[1]/span').click()#详情
        time.sleep(1)
        self.driver.close()

    def test_purchaseOrder_bulkgoods(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[2]').click()#采购订单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[1]/div[2]/div/div/input').click()#状态
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/button').click()#搜索
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/a[2]/span').click()#收货
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/button').click()#批量收货
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/button[1]').click()#确认收货
        time.sleep(1)
        popup = self.driver.find_element_by_xpath('/html/body/div[2]/div')
        popup.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()