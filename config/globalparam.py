#coding=utf-8
#全局变量配置
import os
from  utils.handle_config import Readconfig

#读取文件的路径 os.path.realpath() 获取的该方法所在路径globalparam,py  os.getcwd(）获取的是执行当前脚本的路径 config
config_file_path = os.path.split(os.path.realpath(__file__))[0]
print(os.getcwd())
print(config_file_path)
#读取配置文件路径
read_config = Readconfig(os.path.join(config_file_path, 'config.ini'))
print(os.path.join(config_file_path, 'config.ini'))
#项目路径
prj_path = read_config.getValue('projectConfig', 'project_path')

#日志路径存放
log_path = os.path.join(prj_path, 'report', 'log')

#存放截图路径
screenshot_path = os.path.join(prj_path, 'report', 'screenshot')

#存放测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')

#默认浏览器设置
browsers = 'chrome'

#存放测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

#base_url
base_url='http://localhost:9528/#'