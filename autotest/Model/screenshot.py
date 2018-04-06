import datetime
import os
import time

from jbhautotest.autotest.Model.Model import Basicmodel
from jbhautotest.autotest.Data.basicdate import basicconfig
from jbhautotest.autotest.Model.path import screen_path

def screenshot(driver, fullpath):
    #创建生成截图名称
    if not os.path.exists(fullpath):
        pass
    else:
        os.remove(fullpath)
    #print(os.path.exists(pic_fullpath))
    #根据设置的截图名称创建截图
    driver.get_screenshot(fullpath)
    #print(os.path.exists(pic_fullpath))

 #用于验证该脚本是否有效
if __name__ == '__main__':
    driver = Basicmodel("chrome")
    driver.open('http://www.baidu.com')
    fullpath = screen_path() + '\\'+ basicconfig.now+ '.png'
    print(fullpath)
    driver.get_screenshot(fullpath)
    driver.quit()
