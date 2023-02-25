# coding=utf-8
# 初始化加入日志
import unittest
from utils.handle_log import Log
from public.common import pyselenium
from config import globalparam


class MyTest(unittest.TestCase):
    """
    添加日志记录
    """

    def setUp(self):
        self.logger = Log()
        self.logger.info('######################### START #########################')
        self.dr = pyselenium.PySelenium(globalparam.browsers)
        self.dr.max_window()

    def tearDown(self):
        self.dr.quit()
        self.logger.info('######################### END #########################')
