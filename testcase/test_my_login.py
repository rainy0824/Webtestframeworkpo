# -*- coding: utf-8 -*-
# @Time    : 2022/7/3 12:43
# @Author  : sunxuan
# @Site    : 
# @File    : test_my_login.py

import  allure
import  pytest
from public.pages.login_page import FastLoginPage
from data.login.login_data import login_data

all_data=[('admin','123456','登录成功'),('test','123456','登录成功'),('dd','123456','登录成功')]

def init_data(fixture_value):
    if fixture_value ==all_data[0]:
        return 'data1' #执行参数与 pytest.main(['-sv','-k','data1','test_my_login.py'])相关
    elif fixture_value ==all_data[1]:
        return  'data2'
    else:
        return 'data3'
@pytest.fixture(params=[all_data[0],all_data[1],all_data[2]],ids=init_data)
def login_data_choose(request):
     resp_param =request.param
     print(f'接收参数:{resp_param}')
     yield resp_param

class TestCaseLogin:
    '''
    @pytest.mark.usefixtures('fixture1','fixture2') 先执行fixture1再执行fixture2
    等价与
    @pyetst.mark.usefixtures('fixture2')
    @pyetst.mark.usefixtures('fixture1') 离函数近先执行
    与函数直接传入fixture1不同的是，它无法获取到fixture1装饰的函数的返回值,建议fixture有返回值，建议直接用例传值
    def test(fixture1):pass  =>可以获取fixture1的返回值
    @pytest.mark.usefixtures('fixture1')
    def test():pass   =>则无法获取fixture返回值
    '''
    ##使用parametrize运行所有数据
    @allure.story('登录用例')
    @pytest.mark.parametrize('login_data_params',login_data,ids=['密码错误，登录失败','用户名错误，登录失败','用户名密码正确，登录成功']) #从py文件获取
    ##采用直接传值的方法传入driver ,@pytest.mark.usefixtures('driver')则无法获取返回值
    def test_login(self,driver,login_data_params):
        '''param_info 参数数据'''
        username, password, expected_value =login_data_params
        #初始化Login对象
        login_page =FastLoginPage(driver)
        #执行登录测试并断言
        login_page.run_login_step(username,password,expected_value)

    #  ###使用pytest.fixure运行指定的数据 22
    # def test_login_choose_data(self,driver,login_data_choose):
    #      username,password,expected_value=login_data_choose
    #      print(f'data:{username},{password},{expected_value}')
    #      login_page =FastLoginPage(driver)
    #      # #执行登录测试并断言
    #      login_page.run_login_step(username,password,expected_value)

if __name__ == '__main__':
    # pytest.main(['-sv','test_my_login.py'])
    pytest.main(['-s','-v','-k','data2','test_my_login.py'])  #不指定k参数则运行所有数据 22