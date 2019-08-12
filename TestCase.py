# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2019/8/12 15:05'

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maxmize_window()
driver.find_element_by_id("kw").send_keys("Python")
time.sleep(3)
driver.find_element_by_id("su").click()
driver.quit()

