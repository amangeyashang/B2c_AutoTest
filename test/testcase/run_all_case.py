# -*- coding:utf-8 -*-


_author_ = 'Leo'
__date__ = '2019/8/20 17:08'
import time
import pytest
from HTMLTestRunner_cn import HTMLTestRunner


def allcase():
    case_dir="F:\TOOLS\python\PyCharmProjects\AutoTestDemo\\test\\testcase\\seller\\"
    testcase=pytest.TestSuite()
    discover=pytest.defaultTestLoader.discover(case_dir,
                                                  pattern='*test.py',
                                                  top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    #print(discover)
    for test_suite in discover:
         for test_case in test_suite:
             #添加用例到testcase
             print(test_case)
             testcase.addTest(test_case)
    return testcase
    report = new_report(setting.TEST_REPORT)  # 调用模块生成最新的报告
    send_mail(report)  # 调用发送邮件模块
if __name__=="__main__":
     now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
     report_path="F:\TOOLS\python\PyCharmProjects\AutoTestDemo\\report\\result.html"
     fp=open(report_path,"wb")
     runner = HTMLTestRunner(
         title="吾空花果山B2c项目自动化测试报告",
         description="用例执行情况：",
         stream=fp,
         verbosity=2,
         retry=0,
         save_last_try=True
     )
     runner.run(allcase())
fp.close()