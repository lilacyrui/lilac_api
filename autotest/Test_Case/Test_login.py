#coding = utf-8
import unittest
from jbhautotest.UIautotest.Model.Model import Basicmodel
from jbhautotest.UIautotest.Model.Logger import Log
from jbhautotest.UIautotest.Page.loginandquit import Login
from jbhautotest.UIautotest.Data.basicdate import basicconfig
from jbhautotest.UIautotest.Model.path import screen_path
log = Log()
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = Basicmodel(basicconfig.driver_name)

    def tearDown(self):
        self.driver.quit()

class TestLogin(MyTest):
    '''用户前后台登录'''
    def test_login_front(self):
        '''聚宝汇前台登录'''
        driver =self.driver
        Login.user_login_front(driver)
        text = driver.get_element("xpath","//a[contains(text(),'充值')]").text
        self.assertEqual(text,'充值')
        fullpath = screen_path() + '\\' + "前台登录成功" + basicconfig.now + '.png'
        print(fullpath)
        driver.get_screenshot(fullpath)
        log.info("前台成功登录")


    def test_login_back(self):
        '''聚宝汇后台登录'''
        driver = self.driver
        Login.user_log_back(driver)
        fullpath = screen_path() + '\\' + "后台登录成功" + basicconfig.now + '.png'
        print(fullpath)
        driver.get_screenshot(fullpath)
        log.info("后台登录成功")


if __name__ == '__main__':
    unittest.main(verbosity=2)
