# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import os
import sys
sys.path.append("..")
import time
import logging
import unittest
import subprocess
import HTMLTestRunner
from tools import debug
from public import login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pyfilename = os.path.basename(__file__).split(".")[0]

class Test_license(unittest.TestCase):
    """docstring for 导入授权"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://10.10.3.228/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1apply_for_authorisation(self):
        """申请授权"""
        driver = self.driver
        driver.get(self.base_url + "/")

        # 调用登录
        login.login_server(driver, pyfilename, "test_1apply_for_authorisation")

        modedirc = {"//div[@id='deviceTypeId-targetEl']/table[1]/tbody/tr/td[2]/input" : "控制器",
                    "//div[@id='deviceTypeId-targetEl']/table[2]/tbody/tr/td[2]/input" : "服务器",
                    "//div[@id='deviceTypeId-targetEl']/table[3]/tbody/tr/td[2]/input" : "控制器+服务器",
                    }
        def inputregister():
            """输入申请授权的表单"""
            driver.find_element_by_xpath(".//*[@id='accreditInfo']/table/tbody/tr[1]/td[3]/a").click()   # 点击申请授权

            driver.find_element_by_xpath("//input[@id='aplCompNameId-inputEl']").send_keys("自动化 cody.guo 上海互普信息技术有限公司")
            driver.find_element_by_xpath("//input[@id='aplRegAddrId-inputEl']").send_keys("自动化 cody.guo 灵岩南路295号")
            driver.find_element_by_xpath("//input[@id='aplContacterId-inputEl']").send_keys("自动化 cody.guo")
            driver.find_element_by_xpath("//input[@id='aplPhonenumId-inputEl']").send_keys("18821201646")
            driver.find_element_by_xpath("//input[@id='aplEmailId-inputEl']").send_keys("hp131@hupu.net")
            driver.find_element_by_xpath("//textarea[@id='aplRemarkId-inputEl']").send_keys("自动化 cody.guo 备注信息.")


        for mode in modedirc:
            # 输入表单
            inputregister()
                 
            driver.find_element_by_xpath(mode).send_keys(Keys.SPACE)  # 选择服务器+控制器模式

            driver.find_element_by_xpath("//div[@id='nacApplyLicenseForm']/div[2]/div/div/div[1]/em/button").click()  # 点击提交申请按钮

            # 等待2秒返回提交成功还是失败.
            time.sleep(2)
            returnote = driver.find_element_by_id("messagebox-1001-displayfield-inputEl").text  # 获取返回结果
            #print(returnote)
            if u"申请已提交成功" in returnote:
                logging.info(str(pyfilename) + "-->" + "test_1apply_for_authorisation" + "--> " + str(modedirc[mode]) + "--> " + str(returnote))
            else:
                logging.error(str(pyfilename) + "-->" + "test_1apply_for_authorisation" + "--> " + str(modedirc[mode]) + "--> " + str(returnote))
                assert u"申请已提交成功" in returnote, returnote

            driver.find_element_by_xpath("//button[@id='button-1005-btnEl']").click()  # 点击确定按钮

    def test_2import_license(self):
        """导入授权"""

        driver = self.driver
        driver.get(self.base_url + "/")

        # 调用登录
        login.login_server(driver, pyfilename, "test_2import_license")

        toolsdir = sys.path[0]
        # print(toolsdir)
        toolsfile = toolsdir + "\\tools\\Upload.exe"
        if not os.path.exists(toolsfile):
            toolsfile = os.path.abspath("..") + "\\tools\\Upload.exe"

        #filedir = r"d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
        filedir = r"D:\test.txt"
        subprocess.Popen([toolsfile, '打开', filedir, '300'])

        driver.find_element_by_xpath(".//*[@id='accreditInfo']/table/tbody/tr[2]/td[3]/a").click() # 导入授权

        driver.find_element_by_xpath("//*[@id='upLicenseId-buttonEl']").click() # 浏览
        time.sleep(8)


        driver.find_element_by_xpath("//div[@id='importLicenseForm']/div[2]/div/div/div[1]").click() # 导入
        time.sleep(3)

        returnImport = driver.find_element_by_xpath("//div[@id='messagebox-1001-displayfield-inputEl']").text # 获取导入结果
        #print(returnImport)
        if u"文件导入成功" in returnImport:
            logging.info(str(pyfilename) + "-->" + "test_2import_license" + "--> " + str(returnImport))
        else:
            logging.error(str(pyfilename) + "-->" + "test_2import_license" + "--> " + str(returnImport))
            assert u"文件导入成功" in returnImport, returnImport

        #print(sure_buttonE1)
        driver.find_element_by_id("button-1005-btnEl").click()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    debug.debug(pyfilename)
    unittest.main()
