# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 15:53
# @Author  : sunxuan
# @Site    : 读取配置文件
# @File    : handle_config.py
import configparser
import codecs


class Readconfig(object):
    """
    读取配置文件 .ini 文件格式
    """

    def __init__(self, filepathname):
        '''

        :param filename: 文件名路径
        '''
        with open(filepathname, 'r') as f:
            data = f.read()
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                with codecs.open(filepathname, 'w') as files:
                    files.write(data)
        self.cf = configparser.ConfigParser()
        self.cf.read(filepathname)

    def getValue(self, env, name):
        """
        :param env: [projectConfig]
        :param name: project_path
        :return:
        """
        return self.cf.get(env, name)