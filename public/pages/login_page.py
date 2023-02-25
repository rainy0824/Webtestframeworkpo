# -*- coding: utf-8 -*-
# @Time    : 2022/7/2 23:14
# @Author  : sunxuan
# @Site    : 
# @File    : login_page.py
import  time
from public.pages.home_page import HomePage
from objprint import  op
class FastLoginPage(HomePage):
    def __init__(self, driver):
        super(FastLoginPage, self).__init__(driver)
    def open_login_url(self):
        '''访问url'''
        self.open_url('/login')
        return self
    def login(self, username, password):
        '''登录操作'''
        self.dr.clear_type('name->username', username)
        self.dr.clear_type('name->password', password)
        self.dr.click("xpath->//button[@class='el-button el-button--primary']")
        return  self
    def run_login_step(self,username,password,expected):
        ##执行步骤
        self.open_login_url().login(username,password).sleep().assert_equal(expected)

