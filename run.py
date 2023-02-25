#coding=utf-8
'''总入口执行'''
import  pytest,os
import unittest
from public.common import  HTMLTestRunnerReportEN
import time,platform
from config import globalparam
from public.common import sendmail

def html_run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    if globalparam.current_system == 'Windows':
        reportname = globalparam.report_path + '/' + 'TestResult' + now + '.html'
    elif globalparam.current_system == "Linux":
        reportname = globalparam.report_path + '/' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunnerReportEN.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the  testcase',
            tester= 'Rainy'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

def allure_run():
    pytest.main(['-sv', '--alluredir', './allure-data'])
    # sleep(5)
    os.system('allure generate  ./allure-data   -o ./allure-report --clean ')
if __name__ == '__main__':
    # html_run()
    allure_run()

