# coding=utf-8
from public.pages import baiduIndexPage
from public.common import mytest
from time import sleep
import time
from public.common.public_functions import get_img


class TestBaiduSearch(mytest.MyTest):
    def _search(self, searchKey):
        """封装百度搜索的函数"""
        baidupage = baiduIndexPage.BaiduIndexPage(self.dr)

        baidupage.open_baidu()
        baidupage.input_search_key(searchKey)
        baidupage.click_search_btn()
        sleep(2)
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        pagetitle = baidupage.return_title()
        get_img(self.dr, pagetitle + now + '.png')
        self.assertIn(searchKey, pagetitle)

    def test_search(self):
        """直接搜索 测试 """
        baidupage = baiduIndexPage.BaiduIndexPage(self.dr)
        baidupage.open_baidu()
        baidupage.input_search_key('百度')
        baidupage.click_search_btn()
        sleep(2)
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        pagetitle = baidupage.return_title()
        get_img(self.dr, pagetitle + now + '.png')
        self.assertIn('docker', pagetitle)

    # def test_search_excel(self):
    #     """使用数据驱动,进行测试"""
    #     datas = datainfo.get_xls_to_list('test.xlsx', 'Sheet1')
    #     for data in datas:
    #         self._search(data)


if __name__ == "__main__":
    TestBaiduSearch().main()
