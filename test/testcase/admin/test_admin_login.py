# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2019/12/11 17:35'

from selenium import webdriver
import time
import unittest
import HTMLTestRunner_cn
import os

browser = webdriver.Firefox()
browser.get("http://47.98.233.88:30002/login?service=https%3A%2F%2Fmember.wkhgs.com%2F%2Fwelcome")
browser.find_element_by_id("username").send_keys("admin")
browser.find_element_by_id("password").send_keys("wkhgs123")
browser.find_element_by_class_name("btn-submit").click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="sidebar"]/ul/li[1]/a/span').click()
browser.find_element_by_xpath('//*[@id="MEMBER_LIST"]/a').click()
time.sleep(1)
i = 106
while (i < 200):
    browser.find_element_by_id("btn-add-member").click()
    time.sleep(1)
    browser.find_element_by_id("form-field-mobile").send_keys("18000000",i)
    time.sleep(1)
    browser.find_element_by_id("form-field-password").send_keys("123456")
    time.sleep(1)
    browser.find_element_by_id("id-date-picker-1").send_keys("2019-08-15")
    time.sleep(1)
    browser.find_element_by_id("form-field-idCardName").send_keys("测试账号")
    time.sleep(1)
    browser.find_element_by_id("form-field-email").send_keys("123456@123.com")
    time.sleep(1)
    browser.find_element_by_id("btn-save").click()
    time.sleep(3)
    print("i的次数",i)
    i += 1
    if i == 200:
        print("次数结束")
        continue
        driver.back()
browser.quit()
