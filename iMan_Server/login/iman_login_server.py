# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import HTMLTestRunner


class Login(unittest.TestCase):
    """docstring for login iMan-Server"""
    def setUp(self):
        
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.3.227/admin"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_login_server(self):
        """登录服务器"""
        driver = self.driver  
        # 打开要访问的服务器地址
        print("#" * 30 + "开始访问并登录服务器." + "#" * 30)
        driver.get(self.base_url + "/")

        # 选择登录服务器
        driver.find_element_by_id("tr0").click()

        # 智能等待并输入用户名、密码、公司编码
        driver.find_element_by_id("accountId").send_keys("admin")  #输入用户名
        driver.find_element_by_id("passwordId").send_keys("admin") #输入密码
        driver.find_element_by_id("companycodeId").send_keys("10000000")  #输入公司编码

        # 点击登录按钮
        driver.find_element_by_xpath("//input[@type='submit']").click()

        # # 获取当前登录管理员,是否使用admin登录,错误退出.
        # name = driver.find_element_by_xpath(".//*[@id='panel-1012-body']/div[1]").text
        # if "admin" in name:
        #     print("管理员admin登录成功.")
        # else:
        #     print("管理员admin登录失败.")
        #     sys.exit(1)
        print("#" * 30 + "登录服务器结束." + "#" * 30)
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
