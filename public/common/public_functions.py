# coding=utf-8
# 公共方法
import time
import platform

from config import globalparam


#  判断系统操作类型
def use_platform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print("Call Windows tasks")
    elif (sysstr == "Linux"):
        print("Call Linux tasks")
    else:
        print("Other System tasks")


# 截图放到report下的img目录下 (window 下存放位置 采用反斜杠 \\)
def get_img(dr, filename):
    """
    :param dr:
    :param filename:
    :return:
    """
    if globalparam.current_system == "Linux":
        path = globalparam.screenshot_path + '/' + filename + '.png'
        dr.take_screenshot(path)
    elif globalparam.current_system == "Windows":
        path = globalparam.screenshot_path + '\\' + filename + '.png'
        dr.take_screenshot(path)


def cost_time(func):
    '''耗时'''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        count_time = end_time - start_time
        return count_time
    return wrapper
@cost_time
def qq():
    time.sleep(2)
    print('1111')





if __name__ == '__main__':
    qq()