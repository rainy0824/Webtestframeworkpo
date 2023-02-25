# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 18:27
# @Author  : sunxuan
# @Site    : 处理日志
# @File    : handle_log.py
import logging
import time
import os
from config import globalparam
log_path = globalparam.log_path


class Log(object):
	def __init__(self):
		self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
		print(self.logname)
		self.err_logname = os.path.join(log_path, 'erro_{0}.log'.format(time.strftime('%Y-%m-%d')))
	def __printconsole(self, level, message):
		# 创建一个logger
		logger = logging.getLogger()
		logger.setLevel(logging.DEBUG)
		# 创建一个handler，用于写入正常日志文件
		fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
		fh.setLevel(logging.DEBUG)
		# 创建一个handler，用于写入错误日志文件
		err_fh = logging.FileHandler(self.err_logname, 'a', encoding='utf-8')
		err_fh.setLevel(logging.ERROR)
		# 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		# 定义handler的输出格式
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)
		err_fh.setFormatter(formatter)
		ch.setFormatter(formatter)
		# 给logger添加handler
		logger.addHandler(fh)
		logger.addHandler(err_fh)
		logger.addHandler(ch)
		# 记录一条日志
		if level == 'info':
			logger.info(message)
		elif level == 'debug':
			logger.debug(message)
		elif level == 'warning':
			logger.warning(message)
		elif level == 'error':
			logger.error(message)
		logger.removeHandler(ch)
		logger.removeHandler(fh)
		logger.removeHandler(err_fh)
		# 关闭打开的文件
		fh.close()
		err_fh.close()

	def debug(self, message):
		self.__printconsole('debug', message)

	def info(self, message):
		self.__printconsole('info', message)

	def warning(self, message):
		self.__printconsole('warning', message)

	def error(self, message):
		self.__printconsole('error', message)


import datetime

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Called function: {func.__name__}\n")
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y



import logging
import sys

def log_decorator(level, log_file=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.basicConfig(filename=log_file, level=level, format='%(levelname)s:%(message)s')
            logger = logging.getLogger()
            console_handler = logging.StreamHandler(sys.stdout)
            logger.addHandler(console_handler)
            result = func(*args, **kwargs)
            logging.shutdown()
            return result
        return wrapper
    return decorator

@log_decorator(level=logging.ERROR, log_file='output.txt')
def add(x, y):
    return x + y
import subprocess
def subprocess_check_call():

    print("**** subprocess.check_call ****")
    print("----------")
    result1 = subprocess.run(["ping","192.168.0.58"])

    print("result1:", result1.returncode)
    print("----------")
    result2 = subprocess.run(["ping","192.168.0.58"],stdout=subprocess.PIPE)
    print("result2:", result2.returncode)

def k():
	r = subprocess.run('ping 192.168.0.98 -c 3',
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			stdin=subprocess.PIPE,
			shell=True)
	# print(r.returncode)
	if r.returncode:
		print('失败')
	else:
		print('成功')










if __name__ == '__main__':
	# lg = Log()
	# lg.info('test')
	# lg.error('error')
	# print(add(3, 4))
	# print(add(5, 4))
	# subprocess_check_call()
	k()