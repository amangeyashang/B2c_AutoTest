# -*- coding:utf-8 -*-
import click as click
_author_ = 'Leo'
__date__ = '2019/8/14 15:05'

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

#商品管理-未上架商品
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[7]').click()

#订单管理-订单列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[9]').click()

#订单管理-退货管理
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[10]').click()

#订单管理-订单报表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[11]').click()

#订单管理-线下订单列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[12]').click()

#个人账户-安全设置
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[14]').click()

#评价管理-评价列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[16]').click()

#配送管理-地址信息
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[18]').click()

#配送管理-默认物流公司
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[19]').click()

#配送管理-运费模版
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[20]').click()

#促销管理-优惠券中心
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[22]').click()

#促销管理-简单特价
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[23]').click()

#促销管理-折扣促销
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[24]').click()

#促销管理-买赠满赠
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[25]').click()

#促销管理-加价换购
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[26]').click()

#促销管理-满减促销
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[27]').click()

#促销管理-拼团促销
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[28]').click()

#账号管理-权限管理
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[30]').click()
#浏览器退出
driver.quit()

