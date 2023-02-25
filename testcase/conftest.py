# -*- coding: utf-8 -*-
# @Time    : 2022/7/2 23:53
# @Author  : sunxuan
# @Site    : 
# @File    : conftest.py
import pytest,os,time

from config import globalparam
from  utils.handle_log import Log
from public.common.pyselenium import PySelenium
from  public.pages.login_page import FastLoginPage
from data.login.login_data import login_data
log = Log()
'''
conftest作用范围: suit1->conftest.py test1/test2.py  suit2->conftest test3/test4.py 根目录conftest.py,
 suit1文件夹中的conftest只能在当前模块使用(test1\test2可调用),suit2不可调用,根目录的conftest，都可以调用
(test1/test2/test3/test4)
根目录的conftest 
fixture 级别:scope 范围： session >module>class>function   不能让session 来调用moule ,只能module来调用module或者session
    function：只要test函数中传入都运行，默认是function的scope ,当做参数传递 
    class：每个类型class的所有test函数只运行一次,即便一个类中多个test1 test2 test3都传入了fixture，
    只有test1会执行fixture,test2 test3不会执行
    module：每个模块文件module的所有test函数，只有每个模块里,即便有多个class,只会执行遇到的第一个test函数，只运行一次
    session：每个session只运行一次
如果fixture 没有返回值: 可以使用 @pytest.mark.usefixture('xxx')
如果fixture 有返回值: @pytest.mark.usefixture('xxx')修饰的函数,无法获取返回值,
建议使用传值的方式 def test(self,'fix函数')  
@pytest.mark.usefixture('xxx')可以修饰类、也可以修饰函数(等价),修饰类时会先调用一次，在执行用例,修饰函数时，
修饰哪个函数就在哪个函数执行之前，调用一次。修饰多个函数，则调用第一个修饰的函数，后面修饰的不在调用。

'''

@pytest.fixture(scope="class")
def driver(check_host):
    log.info('######################### START1 #########################')
    dr = PySelenium(globalparam.browsers)
    dr.max_window()
    yield dr
    log.info('######################### END1 #########################')
    time.sleep(3)
    dr.quit()

@pytest.fixture(scope="class")
def user_login(driver):
    '''只登录调用'''
    #初始化login_page
    login_page =FastLoginPage(driver)
    #运行登录用例
    login_page.run_login_step(login_data[2][0],login_data[2][1],login_data[2][2])
    yield driver
    log.info('登录成功')


