# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 19:41
# @Author  : sunxuan
# @Site    : 
# @File    : module_page.py

from public.pages.home_page import HomePage
from config.globalparam import base_url


class FastModulePage(HomePage):
    def __init__(self,driver):
        super(FastModulePage,self).__init__(driver)
    def open_url(self):
        url = base_url +'/auto/module'
        self.dr.open(url)
        return  self
    def add_module(self):
        self.dr.click('id->module_add')

        self.dr.click('class->vue-treeselect__control-arrow-container')
        self.dr.move_to_element('xpath->//*[text()="bug测试"]')

        self.dr.clear_type('id->module_name','123')

        self.dr.click('xpath->//div[@class="el-dialog__body"]//i[@class="el-select__caret el-input__icon el-icon-arrow-up"]')
        self.dr.wait(1)
        self.dr.click('xpath->//body/div[4]/div[1]/div[1]/ul[1]/li[3]')
        self.dr.clear_type('id->module_manager','3432342')
        self.dr.clear_type('id->module_desc','43535345')
        self.dr.click('xpath->//div[@class="el-dialog__body"]//button[@class="el-button el-button--primary"]')
        return self



