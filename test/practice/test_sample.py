# -*- coding:utf-8 -*-
# content of test_sample.py
_author_ = 'Leo'
__date__ = '2019/8/23 10:06'
import pytest
def func(x):
    return x + 1


def test_answer():
    assert func(3)==5