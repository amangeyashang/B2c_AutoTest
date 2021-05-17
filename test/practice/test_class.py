# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2019/8/23 10:33'
#F:\TOOLS\python\PyCharmProjects\AutoTestDemo\test\testcase\test_class.py
import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    pytest.main(['-q', ' test_class.py'])
