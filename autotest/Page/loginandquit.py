# coding =utf-8
import time

from jbhautotest.UIautotest.Data.basicdate import datainfo
from jbhautotest.UIautotest.Model.screenshot import screenshot


class Login:

    # def __init__(self):
    #     self.driver = Basicmodel("chrome")

    def user_login_front(driver):
            driver.open(datainfo.front_Url)
            time.sleep(1)
            driver.max_window()
            driver.clear("xpath", "//*/input[@placeholder='请输入手机号']")
            driver.type_value("xpath", "//*/input[@placeholder='请输入手机号']", datainfo.front_user)
            driver.clear("xpath", "//*/input[@placeholder='请输入短信验证码']")
            driver.type_value("xpath", "//*/input[@placeholder='请输入短信验证码']", datainfo.front_code)
            driver.click("xpath", "//button[contains(text(),'登录')]")
            time.sleep(6)
            # step = "前台登录成功.png"
            # screenshot(driver, step)
            print("----前台登录成功----")
    def user_log_back(driver):
            driver.open(datainfo.back_Url)
            time.sleep(1)
            # driver.max_window()
            driver.clear("xpath", "//input[@placeholder='输入用户名']")
            driver.type_value("xpath", "//input[@placeholder='输入用户名']", datainfo.back_user)
            driver.clear("xpath", "//input[@placeholder='输入密码']")
            driver.type_value("xpath", "//input[@placeholder='输入密码']", datainfo.back_pwd)
            driver.click("xpath", "//button[@type='submit']")
            time.sleep(3)
            # step = "后台登录成功.png"
            # screenshot(driver,step)
            print("----后台登录成功----")


    def user_quit(driver):
        print("----退出----")
        driver.quit()
