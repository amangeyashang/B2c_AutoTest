#-*- coding:utf-8 -*-

_author_ = 'Leo'
__date__ = '2019/8/14 15:05'

from selenium import webdriver
import time
import unittest
import HTMLTestRunner_cn

driver = webdriver.Firefox()
#driver = webdriver.Chrome()


#打开浏览器
driver.get("http://192.168.1.28:8081/")
#浏览器最大化
#driver.maximize_window()

#卖家端-登录
driver.find_element_by_id("login-user").send_keys("18123456789")
driver.find_element_by_id("login-password").send_keys("123456")
driver.find_element_by_id("login-btn").click()
time.sleep(3)

"""
#卖家端-会员注册
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[3]/a").click()
#输入手机号
driver.find_element_by_id("phone").send_keys("18000000000")
#输入密码
driver.find_element_by_id("password").send_keys("123456")
#输入确认密码
driver.find_element_by_id("confirmPswd").send_keys("123456")
#点击【短信校验码】按钮
driver.find_element_by_id("sms-btn").click()
#输入校验码
driver.find_element_by_id("smsCode").send_keys("123456")
#点击【注册】按钮
driver.find_element_by_id("register-btn").click()
#点击【登录】按钮
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/a").click()

#卖家端-忘记密码
driver.find_element_by_link_text("忘记密码？").click()
driver.find_element_by_id("username").send_keys("18000000001")
driver.find_element_by_id("submit-btn").click()
driver.find_element_by_id("sms-btn").click()
driver.find_element_by_id("validateCode").send_keys("123456")
driver.find_element_by_id("submit-btn").click()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("confirmPswd").send_keys("123456")
driver.find_element_by_id("submit-btn").click()
time.sleep(1)

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

#商品管理-商品分类
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[8]').click()

#订单管理-订单列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[10]').click()

#订单管理-退货管理
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[11]').click()

#订单管理-订单报表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[12]').click()

#订单管理-线下订单列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[13]').click()

#促销管理-优惠券中心
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[15]').click()

#促销管理-简单特价
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[16]').click()

#促销管理-折扣促销
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[17]').click()

#促销管理-买赠满赠
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[18]').click()

#促销管理-加价换购
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[19]').click()

#促销管理-满减促销
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[20]').click()

#促销管理-拼团促销
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[21]').click()

#会员管理-会员列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[23]').click()

#会员管理-会员设置
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[24]').click()

#会员管理-会员修改记录
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[25]').click()

#个人账户-安全设置
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[27]').click()

#评价管理-评价列表
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[29]').click()

#账号管理-权限管理
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-list"]/div/ul/li[31]').click()

#卖家端-登出
time.sleep(2)
#点击退出按钮
driver.find_element_by_xpath('//*[@id="headerBar"]/div[1]/div/ul/li/a[2]').click()
#定位弹出对话框
ele_id = driver.switch_to.alert
#点击“确认”
ele_id.accept()
#点击“取消”
#ele_id.dismiss()
"""

#浏览器退出
driver.quit()

