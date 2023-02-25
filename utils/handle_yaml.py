# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 18:04
# @Author  : sunxuan
# @Site    : 
# @File    : handle_yaml.py
import yaml,json
from objprint import op
import  pytest
from config import globalparam
from string import Template

def yaml_to_json(file_path):
    try:
        path = globalparam.prj_path + '/' + file_path
        with open(path, 'r', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            return datas
    except Exception as e:
        raise e

def yaml_template(file_path,replace_data:dict):
    path = globalparam.prj_path + '/' + file_path
    with open(path,encoding="utf-8") as f:
        re = Template(f.read()).safe_substitute(replace_data)
        return yaml.safe_load(re)

if __name__ == '__main__':
    res = yaml_to_json('data/project/demo_testcase_ref.yml')
    op(res)
    project_datas = yaml_to_json('data/project/project_keyword.yaml')

