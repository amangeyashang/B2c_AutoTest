# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/17 14:32'

from selenium import webdriver
import time
import pytest
import os

#商品审核-SPU列表
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

    def test_spuList_spuNameSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[1]').click()#SPU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("菠菜")#spu名称
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[5]/button').click()#筛选
        time.sleep(1)
        self.driver.close()

    def test_spuList_spuCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[1]').click()#SPU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[3]/div[2]/div/input').send_keys("SPU21042600000008")#spu编码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[5]/button').click()#筛选
        time.sleep(1)
        self.driver.close()

    def test_spuList_commodityBrandSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[1]').click()#SPU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[4]/div[2]/div/input').send_keys("鲜货农业")#商品品牌
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[5]/button').click()#筛选
        time.sleep(1)
        self.driver.close()

    def test_spuList_creationTimeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/div').click()#商品审核
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[3]/ul/li[1]').click()#SPU列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[2]/div/div[2]/div/input[1]').click()#创建时间
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-picker-panel.el-date-range-picker.el-popper.has-sidebar.has-time > div.el-picker-panel__body-wrapper > div.el-picker-panel__sidebar")
        option.find_element_by_css_selector("body > div.el-picker-panel.el-date-range-picker.el-popper.has-sidebar.has-time > div.el-picker-panel__body-wrapper > div.el-picker-panel__sidebar > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()