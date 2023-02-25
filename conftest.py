# -*- coding: utf-8 -*-
# @Time    : 2022/7/8 10:51
# @Author  : sunxuan
# @Site    : 
# @File    : conftest.py
#最大
import pytest,subprocess
from retrying import  retry
from utils.handle_log import Log
log=Log()

@pytest.fixture(scope='session')
@retry(stop_max_attempt_number=2,wait_fixed=5)
def check_host():
    '''检查网络'''
    log.info('开始检查网络')
    r = subprocess.run('ping 192.168.0.58 -c 2',
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin=subprocess.PIPE,
                       shell=True)
    if r.returncode:
        log.info('*******网络访问失败*********')
        raise NetWorkError('网络错误')
    else:
        log.info('**********网络正常*********')


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")