# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 19:12
# @Author  : sunxuan
# @Site    :
# @File    : test3.py
import pytest

all_data=[
	(1,2),#正常的数据
	(3,4),#错误的数据
	(5,6) #无效的数据
]

def run_need_data(get_fixture):
	if get_fixture ==all_data[0]:
		return "correct_data"
	elif get_fixture ==all_data[1]:
		return "wrong_data"
	else:
		return 'abandon_data'
@pytest.fixture(params=[all_data[0],all_data[1],all_data[2]],ids=run_need_data)
def get_choose_data(request):
	req_param= request.param
	print(f'start insert:{req_param}.....')
	print('--------------------------------')
	yield  req_param
	print(f'end insert:{req_param}.....')
	print('--------------------------------')

class TestKey:
	# @pytest.mark.parametrize('a,b',[(3,5),(6,8),(9,12)],ids=['first data','second data','third data'])
	# def test_key(self,a,b,get_Key):
	# 	print('--------------------------------')
	# 	print(f'test sum:{a+b}')
	# 	print('--------------------------------')
	# 	print(f'get_Key:{get_Key}')

	def test_choose(self,get_choose_data):
		result =get_choose_data[0]*get_choose_data[1]
		print(f'result:{result}')
if __name__ == '__main__':
	#输入k 按指定参数  从所有数据中运行指定的数据
	pytest.main(["-s",'-k','correct_data', "test3.py",])
