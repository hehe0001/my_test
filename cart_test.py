#!/user/bin/env python
#  _*_ coding:utf-8 _*_
import pytest


def f():
    return 3


def test_function():
    assert f() == 3