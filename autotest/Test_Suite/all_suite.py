#coding = utf-8
import time
import unittest
from jbhautotest.UIautotest.Model.HTMLTestRunner import HTMLTestRunner
from jbhautotest.UIautotest.Model.sendmail import Sendmail
from jbhautotest.UIautotest.Data.basicdate import basicconfig
from jbhautotest.UIautotest.Model.findfile import getfile
from jbhautotest.UIautotest.Model.path import report_path,testcase_path
import os

# suite = unittest.TestSuite()
# #suite.addTest(TestLogin("test_login_front"))
# suite.addTest(TestRecharge("test_recharge"))
# #suite.addTest(TestLogin("test_quit"))
def suite_all():
    #获取所有以Test_开头的测试用例
    Discover = unittest.defaultTestLoader.discover(testcase_path(), pattern=basicconfig.case_pattern)
    # 创建生成报告名称 ：报告存放地址+ \\+ 报告名称（日期时间+report）
    filename = report_path() + '\\' + basicconfig.now +'_'+'report.html'
    print(filename)
    #打开文件
    fp = open(filename,'wb')
    #设置报告名称、描述
    runner = HTMLTestRunner(stream=fp, title=basicconfig.report_title, description=basicconfig.report_description)
    #执行测试用例写入报告
    runner.run(Discover)
    fp.close()
    #获取新生成的报告，发送邮件
    # new_report = getfile()
    # Sendmail(new_report)
if __name__ == '__main__':
    print(report_path())
    suite_all()
