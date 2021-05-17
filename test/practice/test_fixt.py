# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2019/8/23 15:07'

import pytest


#不带参数时默认scope="function"
@pytest.fixture()
def login():
    print("输入账号：密码先登录")

def test_s1(login):
    print("用例1：登录之后其它动作1")

def test_s2():#不传login
    print("用例2：不需要登录，操作2")
def test_s3(login):
    print("用例3：登录之后其它动作3")


if__name__=="__main__":
    pytest.main([""])