# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/13 15:51'

from selenium import webdriver
import time
import pytest
import os
import random

#商品管理-上架管理
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

    def test_theGoodsAreonTheShelves_productNameSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys("百香果 500g")#商品名称
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button/span').click()
        time.sleep(1)
        self.driver.close()

    def test_theGoodsAreonTheShelves_barCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[3]/div[2]/div/input').send_keys("19112800000005")#商品条码
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_theGoodsAreonTheShelves_scatteredSaidScreening(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/div[2]/div/div/input').click()#是否散称
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_theGoodsAreonTheShelves_PresaleMerchandiseScreening(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[5]/div[2]/div/div/input').click()#是否预售
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_theGoodsAreonTheShelves_compile(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[2]/button[1]').click()#编辑
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/div/input').send_keys(random.randint(0,100))
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[7]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[7]/div/div/input').send_keys(random.randint(0,100))
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/div/input').send_keys(random.randint(0,100))
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[9]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[9]/div/div/input').send_keys(random.randint(0,100))
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        self.driver.close()

    def test_theGoodsAreonTheShelves_unShelve(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[11]/div/span').click()#下架
        time.sleep(1)
        self.driver.find_element_by_css_selector("body > div.ui-popup.ui-popup-show.ui-popup-focus > div > table > tbody > tr:nth-child(3) > td > div.ui-dialog-button > button.ui-dialog-autofocus").click()
        time.sleep(1)
        self.driver.close()

    def test_theGoodsAreonTheShelves_derivedData(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[2]').click()#上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[1]/div/input').click()#导出数据
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()#所选项
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[1]/div/input').click()#导出数据
        time.sleep(1)
        option.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()#当前页
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()