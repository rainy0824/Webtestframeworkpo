# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 11:37
# @Author  : sunxuan
# @Site    : 
# @File    : test_my_project.py
import  allure
import  pytest,os,time
from  utils.handle_yaml import yaml_to_json
from  public.pages.project_page import FastProjectPage
#从py文件获取data
from data.project.project_data import project_data
#从yaml获取data
project_data_yaml =yaml_to_json('data/project/project.yaml')



class TestCaseProject:
    # @allure.title('添加项目')
    #传递fixture
    @allure.story("添加项目用例")
    @pytest.mark.parametrize('project_data_params',project_data)
    def test_add_project(self,user_login,project_data_params):
        ''' fixure:user_login 返回一个dirver
        1.登录成功
        2.打开界面
        3.点击添加
        4.添加完毕
        5.断言
        '''
        project_name,project_desc,project_manager,project_developer,project_tester,expected =project_data_params
        project_page =FastProjectPage(user_login)
        project_page.run_add_project_step(project_name,project_desc,project_manager,project_developer,project_tester,expected)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_my_project.py'])
    # pytest.main(['-sv', 'test_my_project.py','--alluredir', './allure-data'])
    # os.system('allure generate  ./allure-data   -o ./allure-report --clean ')


