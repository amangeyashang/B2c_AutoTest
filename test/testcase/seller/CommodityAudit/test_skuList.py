# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/17 17:17'

from selenium import webdriver
import time
import pytest
import os

#商品审核-SKU列表
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

    def test_skuList_spuCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[2]').click()#SKU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[1]/div[2]/div/input').send_keys("SPU21042600000009")#SPU编码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[5]/button').click()#筛选
        time.sleep(1)
        self.driver.close()

    def test_skuList_skuCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[2]').click()#SKU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys("SKU21042600000008")#SKU编码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[5]/button').click()#筛选
        time.sleep(1)
        self.driver.close()

    def test_skuList_barCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[2]').click()#SKU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[3]/div[2]/div/input').send_keys("1231545")#商品条码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[5]/button').click()#筛选
        time.sleep(1)
        self.driver.close()

    def test_skuList_creationTimeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[2]').click()#SKU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/div[2]/div/input[1]').click()#创建时间
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-picker-panel.el-date-range-picker.el-popper.has-sidebar.has-time > div.el-picker-panel__body-wrapper > div.el-picker-panel__sidebar")
        option.find_element_by_css_selector("body > div.el-picker-panel.el-date-range-picker.el-popper.has-sidebar.has-time > div.el-picker-panel__body-wrapper > div.el-picker-panel__sidebar > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.close()

    def test_skuList_seeDetails(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[2]').click()#SKU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/a[2]/span').click()#查看详情
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()