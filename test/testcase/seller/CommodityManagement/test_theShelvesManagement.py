# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/14 16:14'

from selenium import webdriver
import time
import pytest
import os
import random

#商品管理-下架管理
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

    def test_goodsNotOnTheShelves_productNameSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys("凤梨 500g")#商品名称
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_goodsNotOnTheShelves_barCodeSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[3]/div[2]/div/input').send_keys("00000003")#商品条码
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_goodsNotOnTheShelves_scatteredSaidScreening(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/input').click()#是否散称
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_goodsNotOnTheShelves_PresaleMerchandiseScreening(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[5]/div[2]/div/div[1]/input').click()#是否预售
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)").click()
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[1]/div/div[6]/button').click()
        time.sleep(1)
        self.driver.close()

    def test_goodsNotOnTheShelves_modification(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[12]/div/span[1]').click()#修改
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[11]/div/div/input').clear()#成本价
        costPrice = str(round(random.uniform(0,40),2))
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[11]/div/div/input').send_keys(costPrice)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[12]/div/div/input').clear()#市场价
        marketPrice = str(round(random.uniform(0,80),2))
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[12]/div/div/input').send_keys(marketPrice)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[13]/div/div/input').clear()#销售价
        salePrice = str(round(random.uniform(0,100),2))
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[13]/div/div/input').send_keys(salePrice)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[14]/div/div/input').clear()#库存
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[14]/div/div/input').send_keys(random.randint(0,100))
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="release-commodity"]/div[2]/form/div[17]/div/button').click()#保存
        time.sleep(1)
        self.driver.close()

    def test_goodsNotOnTheShelves_putaway(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[12]/div/span[2]').click()#上架
        time.sleep(1)
        self.driver.close()

    def test_goodsNotOnTheShelves_derivedData(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_class_name("el-icon-menu").click()#商品管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[2]/ul/li[3]').click()#下架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="shelf-item"]/div[2]/div[2]/div[1]/div[1]/input').click()#导出数据
        time.sleep(1)
        option = self.driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul")
        option.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()