#coding = utf-8
import time
import unittest

from jbhautotest.UIautotest.Model.Model import Basicmodel
from jbhautotest.UIautotest.Model.Logger import Log
from jbhautotest.UIautotest.Page.loginandquit import Login
from jbhautotest.UIautotest.Page.Recharge import Recharge
from jbhautotest.UIautotest.Data.basicdate import basicconfig
from jbhautotest.UIautotest.Model.path import screen_path
log = Log()
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = Basicmodel(basicconfig.driver_name)

    def tearDown(self):
        self.driver.quit()

class TestRecharge(MyTest):
    def test_recharge(self):
        '''主卡充值'''
        driver = self.driver
        Login.user_login_front(driver)
        time.sleep(3)
        log.info("后台登录成功")
        Recharge.recharge(driver)
        fullpath = screen_path() + '\\' + "充值成功" + basicconfig.now + '.png'
        print(fullpath)
        driver.get_screenshot(fullpath)
        log.info("充值成功")



if __name__ == '__main__':
    unittest.main(verbosity=2)