# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'

import os
import sys
sys.path.append("..")
import time
import unittest
import logging
import HTMLTestRunner
from public import login
from tools import debug
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


pyfilename = os.path.basename(__file__).split(".")[0]

# print(os.path.abspath(".."))
# debug.debug("iman_login_server")

class Login(unittest.TestCase):
    """docstring for 登录服务器"""
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://10.10.3.228/admin"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_login_server(self):
        """登录服务器"""
        driver = self.driver
        driver.get(self.base_url + "/")

        # 调用登录接口
        login.login_server(driver, pyfilename, "test_login_server")

        returnlogin = driver.find_element_by_xpath("//*[@id='panel-1012-body']/div[1]").text
        loginName = returnlogin.split("：")[1].split("\n")[0]
        if "admin" == loginName:
            logging.info(str(pyfilename) + "-->" + "test_login_server" + "--> " + str(returnlogin.split("\n")[0]))
        else:
            logging.error(str(pyfilename) + "-->" + "test_login_server" + "--> " + str(returnlogin.split("\n")[0]))
            assert "admin" == loginName, loginName

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    debug.debug(pyfilename)
    unittest.main()
