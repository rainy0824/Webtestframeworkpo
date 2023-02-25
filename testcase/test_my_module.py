# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 19:36
# @Author  : sunxuan
# @Site    : 
# @File    : test_my_module.py
import  allure
import  pytest
from data.module.module_data import module_success_data
from  public.pages.module_page import FastModulePage
class TestCaseMoudle:
    @allure.title('添加模块')
    #传递fixture
    @pytest.mark.parametrize('module_data',module_success_data)
    def test_add_module(self,user_login,module_data):
        '''
        1.登录成功
        2.打开界面
        3.点击添加
        4.添加完毕
        5.断言
        '''
        parent_module_id,module_name,module_project_id,module_manager,module_desc,expected =module_data
        module_page =FastModulePage(user_login)
        #登录成功后跳转模块管理
        module_page.open_url()
        #添加项目
        module_page.add_module(module_name,module_desc,module_manager,module_developer,module_tester)
        #'断言'
        result =module_page.add_module_is_success()

        assert  result == expected
    def test_module(self,user_login):
        module_page=FastModulePage(user_login)
        module_page.open_url()
        module_page.add_module()
        allure.attach(module_page.dr.take_screenshot_as_png(),name='截图',attachment_type='png')



if __name__ == '__main__':
    pytest.main(['-sv','test_my_module.py'])

