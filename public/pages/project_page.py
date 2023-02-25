# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 11:59
# @Author  : sunxuan
# @Site    : 
# @File    : project_page.py

from public.pages.home_page import HomePage

class FastProjectPage(HomePage):
    def __init__(self, driver):
        super(FastProjectPage, self).__init__(driver)

    def open_project_url(self):

        self.open_url('/auto/project')
        return self

    def add_project(self, project_name, project_desc, project_manager, project_developer, project_tester):
        self.dr.click('id->project_add')
        self.dr.clear_type('id->project_name', project_name)
        self.dr.clear_type('id->project_desc', project_desc)
        self.dr.clear_type('id->project_manager', project_manager)
        self.dr.clear_type('id->project_developer', project_developer)
        self.dr.clear_type('id->project_tester', project_tester)
        self.dr.click('xpath->//div[@class="el-dialog__footer"]//button[@class="el-button el-button--primary"]')
        return self

    def run_add_project_step(self, project_name, project_desc, project_manager, project_developer, project_tester,
                             expected):
        self.sleep(2).open_project_url()\
            .add_project(project_name, project_desc, project_manager, project_developer,
                                            project_tester)\
            .sleep(1)\
            .save_screen()\
            .assert_equal(expected).sleep(1)
