import  pytest

@pytest.fixture(scope='module')
def deal_01():
    print('没有返回值的fixture')

@pytest.fixture(scope='class')
def deal_02():
    print('有返回值的fixture')
    a='001'
    yield a
    print('调用完毕')
