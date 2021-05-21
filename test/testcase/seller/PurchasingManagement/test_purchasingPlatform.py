# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/18 17:27'

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

    def test_purchasingPlatform_productNameSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[1]').click()#采购平台
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("薄皮青椒")#商品名称
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[6]').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchasingPlatform_barCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[1]').click()#采购平台
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[3]/div[2]/div/input').send_keys("133215")#商品条码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[6]').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchasingPlatform_skuCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[1]').click()#采购平台
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[4]/div[2]/div/input').send_keys("SKU21042600000009")#SKU编码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[6]').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchasingPlatform_spuCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[1]').click()#采购平台
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[5]/div[2]/div/input').send_keys("SKU21042600000009")#SPU编码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div[1]/div[6]').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_purchasingPlatform_AddThePurchasing(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/div/span').click()#采购管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[9]/ul/li[1]').click()#采购平台
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span').click()#全选
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/button').click()#开始采购
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/button').click()#加入采购单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div/button[2]').click()#确认采购
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/button[1]').click()#生成采购订单
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    pytest.main()