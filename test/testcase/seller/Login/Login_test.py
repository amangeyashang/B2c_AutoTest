# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2019/8/19 16:31'

from selenium import webdriver
import time
import pytest
import os


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

    #测试用例 B2C_seller-login-001
    def test_login_user_error(self):
        #用户名错误,密码正确
        self.login('180000000003','123456') #输入错误的用户名和正确的密码
        time.sleep(2)
        error_message = self.driver.find_elements_by_class_name("go-ui-link")
        result = self.driver.find_elements_by_xpath('//*[@id="headerBar"]/div[1]/div/ul/li/a[1]/span')
        if result != error_message:
            print("测试用例 B2C_seller-login-001"+"执行用例成功")
        else:
            self.driver.get_screenshot_as_file(
                "F:\TOOLS\python\PyCharmProjects\B2c_AutoTest\screenshot\login_user_error.png")
            print("测试用例 B2C_seller-login-001"+"执行测试失败")
        self.driver.close()

    #测试用例 B2C_seller-login-002
    def test_login_pwd_error(self):
        #用户名正确，密码错误
        self.login('18000000003','1234567') #输入正确的用户名和错误的密码
        time.sleep(2)
        error_message = self.driver.find_elements_by_class_name("go-ui-link")
        result = self.driver.find_elements_by_xpath('//*[@id="headerBar"]/div[1]/div/ul/li/a[1]/span')
        if result != error_message:
            print("测试用例 B2C_seller-login-002"+"执行用例成功")
        else:
            self.driver.get_screenshot_as_file(
                "F:\TOOLS\python\PyCharmProjects\B2c_AutoTest\screenshot\login_pwd_error.png")
            print("测试用例 B2C_seller-login-002"+"执行用例失败")
        self.driver.close()

    #测试用例 B2C_seller-login-003
    def test_login_user_null_error(self):
        #用户名为空，密码正确
        self.login(' ', '123456')  # 输入正确的用户名和错误的密码
        time.sleep(2)
        error_message = self.driver.find_elements_by_class_name("go-ui-link")
        result = self.driver.find_elements_by_xpath('//*[@id="headerBar"]/div[1]/div/ul/li/a[1]/span')
        if result != error_message:
            print("测试用例 B2C_seller-login-003"+"执行用例成功")
        else:
            self.driver.get_screenshot_as_file(
                "F:\TOOLS\python\PyCharmProjects\B2c_AutoTest\screenshot\login_user_null.png")
            print("测试用例 B2C_seller-login-003"+"执行用例失败")
        self.driver.close()

    #测试用例 B2C_seller-login-004
    def test_login_success(self):
        #用户名、密码正确
        self.login('18000000003','123456') #输入正确的用户名和密码
        time.sleep(2)
        login_success = self.driver.find_elements_by_xpath('//*[@id="headerBar"]/div[1]/div/ul/li/a[1]/span')
        time.sleep(3)
        result = self.driver.find_elements_by_class_name("pickSelfBtn")
        if result != login_success:
            print("测试用例 B2C_seller-login-004"+"执行用例成功")
        else:
            self.driver.get_screenshot_as_file(
                "F:\TOOLS\python\PyCharmProjects\B2c_AutoTest\screenshot\login_error.png")
            print("测试用例 B2C_seller-login-004"+"执行用例失败")
        self.driver.close()

if __name__ == "__main__":
    pytest.main()