# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 16:11
# @Author  : sunxuan
# @Site    : 
# @File    : aa.py
import pytest

@pytest.mark.only_run
def test1():
	print('test1')


def test2():
	print('test2')


def test3():
	print('test3')


def test4():
	print('test4')


def test5():
	print('test5')
if __name__ == '__main__':
    pytest.main(['-sv','aa.py','-m=only_run'])