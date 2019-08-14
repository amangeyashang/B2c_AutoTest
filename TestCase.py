# -*- coding:utf-8 -*-
import click as click
_author_ = 'Leo'
__date__ = '2019/8/12 15:05'

from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
driver = webdriver.Firefox()
#打开浏览器
driver.get("https://merch.wkhgs.com/")
#浏览器最大化
#driver.maximize_window()

#卖家端-登录
driver.find_element_by_id("login-user").send_keys("18000000003")
driver.find_element_by_id("login-password").send_keys("123456")
driver.find_element_by_id("login-btn").click()
time.sleep(3)

#店铺装饰-店铺基础数据
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[2]').click()

#店铺装饰-装饰店铺
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[3]').click()

#商品管理-发布商品
#10秒内每隔500毫秒扫描1次页面变化 wait = ui.WebDriverWait(driver,10)
# 当出现指定的元素后结束  wait.until(lambda driver: driver.find_element_by_id("publicProduct"))
time.sleep(1)
driver.find_element_by_id("publicProduct").click()

#商品管理-已上架商品
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[6]').click()

#退出浏览器
driver.quit()

