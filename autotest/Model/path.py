import unittest
import os
from jbhautotest.UIautotest.Data.basicdate import basicconfig

def report_path():
    #cur_path = os.path.dirname(os.getcwd())
    # _path是存放报告的路径
    report_path = os.path.join(os.path.dirname(basicconfig.base_path + basicconfig.result_path), basicconfig.report_dir)
    #创建报告目录
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    #按日期生成子目录
    report_path = os.path.join(os.path.dirname(report_path + '\\'), basicconfig.now_date)
    # 如果不存在这个log文件夹，就自动创建一个
    #创建子目录
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    return report_path

def log_path():
    #cur_path = os.path.dirname(os.getcwd())
    # log_path是存放日志的路径
    log_path = os.path.join(os.path.dirname(basicconfig.base_path + basicconfig.result_path), basicconfig.log_dir)
    #创建日志目录
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    #按日期创建子目录
    log_path = os.path.join(os.path.dirname(log_path + '\\'), basicconfig.now_date)
    # 如果不存在这个log文件夹，就自动创建一个
    #print(log_path)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    return log_path

def screen_path():
    #cur_path = os.path.dirname(os.getcwd())
    # _path是存放截图的路径
    screen_path = os.path.join(os.path.dirname(basicconfig.base_path + basicconfig.result_path), basicconfig.screen_dir)
    #创建截图目录
    if not os.path.exists(screen_path):
        os.mkdir(screen_path)
    screen_path = os.path.join(os.path.dirname(screen_path + '\\'), basicconfig.now_date)
    # 按日期创建子目录
    if not os.path.exists(screen_path):
        os.mkdir(screen_path)
    return screen_path
def testcase_path():
    #cur_path = os.path.dirname(os.getcwd())
    # _path是存放截图的路径
    case_path = os.path.join(os.path.dirname(basicconfig.base_path + basicconfig.case_path))
    return case_path


if __name__ == '__main__':
    print(report_path())
    print(log_path())
    print(screen_path())
    print(testcase_path())