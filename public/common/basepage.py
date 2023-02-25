# coding=utf-8
# 公共基类
import allure
import time

from  utils.handle_yaml import yaml_template,yaml_to_json
from objprint import  op
class BasePage:
    '''封装driver'''

    def __init__(self, selenium_driver):
        self.dr = selenium_driver  #pyselenium
        self.text='init_text' #文本信息


