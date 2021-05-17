#在配置文件、静态资源的管理，遵循高内聚低耦合原则
# _*_ coding:utf-8 _*_
__author__ = 'Leo'

import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR,"config")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testcase")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"log")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"data")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")
# 驱动文件
DRIVER_DIR = os.path.join(BASE_DIR,"drivers")

