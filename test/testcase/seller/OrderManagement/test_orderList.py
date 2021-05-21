# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/5/17 18:35'

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

    def test_orderList_obligation_orderNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[2]').click()#待付款
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input').send_keys("STMASTER20102800001")#订单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_obligation_mobileNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[2]').click()#待付款
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("18716280028")#手机号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_obligation_seeDetails(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[2]').click()#待付款
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/div').click()#查看详情
        time.sleep(1)
        self.driver.close()

    def test_orderList_obligation_cancelOrder(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[2]').click()#待付款
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div[2]').click()#取消订单
        time.sleep(2)
        window = self.driver.find_element_by_css_selector("#order-list > div.el-dialog__wrapper > div")
        window.find_element_by_css_selector("#order-list > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary").click()
        time.sleep(5)
        self.driver.close()

    def test_orderList_WaitingList_orderNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[3]').click()#待接单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input').send_keys("STMASTER20102800001")#订单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_WaitingList_mobileNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[3]').click()#待接单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("18716280028")#手机号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_ForPicking_orderNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[4]').click()#待拣货
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input').send_keys("STMASTER20102800001")#订单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_ForPicking_mobileNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[4]').click()#待拣货
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("18716280028")#手机号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_StayToThe_orderNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[5]').click()#待自提
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input').send_keys("GIMASTER20122100002")#订单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_StayToThe_mobileNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[5]').click()#待自提
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("18716280028")#手机号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_StayToThe_seeDetails(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[5]').click()#待自提
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/div').click()#查看详情
        time.sleep(1)
        self.driver.close()

    def test_orderList_StayToThe_verify(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[5]').click()#待自提
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div[2]').click()#自提校验
        time.sleep(1)
        window = self.driver.find_element_by_xpath('//*[@id="order-list"]/div[4]/table')
        window.find_element_by_xpath('//*[@id="order-list"]/div[4]/table/tr[2]/td/ul/li/input').send_keys("123456")#输入提货码
        window.find_element_by_xpath('//*[@id="order-list"]/div[4]/table/tr[3]/td/div/button[1]').click()#确认
        time.sleep(5)
        self.driver.close()

    def test_orderList_StayToThe_cancelOrder(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[5]').click()#待自提
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="cancelBtn"]').click()#取消订单
        time.sleep(1)
        window = self.driver.find_element_by_xpath('//*[@id="order-list"]/div[5]/div')
        window.find_element_by_xpath('//*[@id="order-list"]/div[5]/div/div[3]/span/button[2]').click()
        time.sleep(5)
        self.driver.close()

    def test_orderList_completed_orderNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[6]').click()#已完成
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input').send_keys("STMASTER21040700003")#订单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_completed_mobileNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[6]').click()#已完成
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("18716280028")#手机号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_completed_seeDetails(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[6]').click()#已完成
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div/div/div').click()#查看详情
        time.sleep(1)
        self.driver.close()

    def test_orderList_canceled_orderNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[7]').click()#已取消
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input').send_keys("STMASTER21051200005")#订单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_canceled_mobileNumberSearch(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[7]').click()#已取消
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input').send_keys("18716280028")#手机号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[2]/div[3]/div').click()#搜索
        time.sleep(1)
        self.driver.close()

    def test_orderList_canceled_seeDetails(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[7]').click()#已取消
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/div').click()#查看详情
        time.sleep(2)
        self.driver.close()

    def test_orderList_canceled_DeleteOrder(self):
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/div/span').click()#订单管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-list"]/ul/li[4]/ul/li[1]').click()#订单列表
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[1]/ul/li[7]').click()#已取消
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="order-list"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div/div[2]').click()#删除订单
        time.sleep(1)
        window = self.driver.find_element_by_xpath('//*[@id="order-list"]/div[5]/div')
        window.find_element_by_xpath('//*[@id="order-list"]/div[5]/div/div[3]/span/button[2]').click()
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    pytest.main()