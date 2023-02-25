# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 12:51
# @Author  : sunxuan
# @Site    : 将每个页面通用的方法提出来
# @File    : home_page.py
import  time,allure
from public.common.basepage import BasePage
from config.globalparam import base_url
from objprint import  op
class HomePage(BasePage):
    def __init__(self,driver):
        super(HomePage,self).__init__(driver)

    def open_url(self,relative_path):
        self.dr.open(base_url + relative_path)

    def sleep(self, sec=1):
        time.sleep(sec)
        return self

    def get_message_text(self):
        '''获取提示语'''
        # 重新给父类text赋值
        self.text = self.dr.get_text('xpath->//div[@role="alert"]//p[@class="el-message__content"]')
        op(f'结束：{self.text}')
        return self.text

    def assert_equal(self, hope_value):
        '''断言'''
        op(f'结果:{self.get_message_text()},期望:{hope_value}')
        assert self.get_message_text() == hope_value
        return self
    #截图
    def save_screen(self, pic_title=None, secs=2):
        time.sleep(secs)
        if not pic_title:
            pic_title= time.strftime('%Y-%m-%d_%H_%M_%S')
        allure.attach(self.dr.origin_driver.get_screenshot_as_png(),pic_title , allure.attachment_type.PNG)
        return self