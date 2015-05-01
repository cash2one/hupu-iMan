# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import os
import sys
sys.path.append("..")
import time
import subprocess
from selenium.webdriver.common.keys import Keys
from public import login
import unittest
import HTMLTestRunner
from selenium import webdriver


class Test_case(unittest.TestCase):
    """docstring for Test_case"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.3.227/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_import_license(self):
        """导入授权"""

        driver = self.driver
        driver.get(self.base_url + "/")
        # 调用登录

        login.login_server(driver)
        
        import_buttonE1 = "button-1037-btnEl"  # 导入按钮
        sure_buttonE1 = "button-1005-btnEl"    # 确定按钮


        print("#" * 30 + "导入授权开始" + "#" * 30)

        # uploaddir = os.getcwd()
        # uploaddir = uploaddir.split("\\home")[0]
        toolsdir = os.path.abspath("..")
        print(toolsdir)
        toolsfile = toolsdir + "\\tools\\upload.exe"
        if not os.path.exists(toolsfile):
            tooslfile = sys.path[0] + "\\tools\\upload.exe"

        #filedir = r"d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
        filedir = r"D:\test.txt"
        subprocess.Popen([tooslfile,'2', filedir])

        driver.find_element_by_xpath(".//*[@id='accreditInfo']/table/tbody/tr[2]/td[3]/a").click()
        time.sleep(1)
        print("正在定位....")
        #self.find_element_by_xpath(".//*[@id='upLicenseId-browseButtonWrap']/div/em/button").click()
        driver.find_element_by_xpath("//*[@id='upLicenseId-buttonEl']").click()
        time.sleep(8)


        driver.find_element_by_id(import_buttonE1).click()
        time.sleep(3)

        messagebox = driver.find_element_by_xpath("//div[@id='messagebox-1001-displayfield-inputEl']").text
        #print(messagebox)
        assert r"文件导入成功" in messagebox, messagebox

        #print(sure_buttonE1)
        driver.find_element_by_id(sure_buttonE1).click()
        
        print("#" * 30 + "导入授权结束" + "#" * 30)
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
