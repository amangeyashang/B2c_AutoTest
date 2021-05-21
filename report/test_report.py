# -*- coding:utf-8 -*-

_author_ = 'Leo'
__date__ = '2019/8/14 15:36'
from HTMLTestRunner_cn import HTMLTestRunner
import os
import unittest
import time

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(allcase)
    runner = HTMLTestRunner(
        title="吾空花果山B2c项目自动化测试报告",
        description="用例测试情况",
        stream=open("./demo.html", "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True)
    # 开始执行测试套件
    runner.run(suite)
