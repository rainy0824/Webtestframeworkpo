# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 20:32
# @Author  : sunxuan
# @Site    : 
# @File    : handle_exception.py
from  retrying import retry,Retrying


class NetWorkError(Exception):
    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return repr('NetWorkError')

def retry_if_network_error(args):
    return isinstance(args,IOError)
def retry_if_type_error(args):
    return isinstance(args,TypeError)

'''
stop_max_attempt_number 最大重试次数
stop_max_delay=10000(最大延迟时间ms,被装饰的函数开始执行的时间点开始，到函数成功运行结束或者失败报错中止的时间点，只要这段时间超过10秒，函数就不会再执行了)
wait_fixed 重试执行间隔时间ms
wait_incrementing_increment 每调用一次增加固定时长ms
retry_on_exception  如果装饰的函数抛出了异常，会去retry_on_exception指向的函数去判断函数返回结果，True则运行指定重试次数，False直接抛出异常
'''
########默认#######
@retry(stop_max_attempt_number=5,retry_on_exception=retry_if_network_error)
def retry_test():
    print('执行')
    # raise IOError
    raise IndexError
#

##########重写retry###################
def retry_handle(retry_time:float,retry_interval:float,retry_on_exception:[BaseException],*args,**kwargs):
    '''
    重写retry默认装饰器
    :param retry_time: 重试次数 s
    :type retry_time:
    :param retry_interval: 重试间隔时间 s
    :type retry_interval:
    :param retry_on_exception: 重试类型
    :type retry_on_exception:
    :param args:
    :type args:
    :param kwargs:
    :type kwargs:
    :return:
    :rtype:
    '''
    def is_exception(exceptions:[BaseException]):
            for exp in retry_on_exception:
                if isinstance(exceptions,exp):
                    return  True
    def _retry(*args,**kwargs):
            return  Retrying(wait_fixed=retry_interval*1000).fixed_sleep(*args,**kwargs)
    return retry(
        wait_func=_retry,
        stop_max_attempt_number=retry_time,
        retry_on_exception=is_exception
    )

@retry_handle(retry_time=3,retry_interval=2,retry_on_exception=[IOError,IndexError])
def retry_test1(data):
    print('执行')
    if data ==1:
        raise   IndexError
    if data ==2:
        raise  IOError


import subprocess
# @retry_handle(retry_time=3,retry_interval=10,retry_on_exception=[IOError])
@retry(stop_max_attempt_number=2,wait_fixed=5)
def check_host():
    '''检查网络'''
    print('开始检查网络')
    r =subprocess.run('ping 192.168.0.58 -c 2',
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin=subprocess.PIPE,
                       shell=True)
    if r.returncode:
        print('*******网络访问失败*********')
        raise MyError("网络异常")
    else:
        print('**********网络正常*********')


if __name__ == '__main__':
    # retry_test()
    # retry_test1(1)
    check_host()