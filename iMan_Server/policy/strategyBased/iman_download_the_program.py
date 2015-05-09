# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'

import os
import sys
sys.path.append("../..")
import time
import unittest
import logging
import subprocess
import HTMLTestRunner
from public import login
from tools import debug
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


pyfilename = os.path.basename(__file__).split(".")[0]

def downloadProgram(self):
    self.find_element_by_id("btnE00").click() # 策略
    self.find_element_by_id("ext-gen1194").click() # 策略基础
    self.find_element_by_id("downloadProgramManageId-btnWrap").click() # 下载程序管理

class Test_download_program(unittest.TestCase):
    """docstring for 下载程序管理,上传软件"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://10.10.3.228/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1uploadPro(self):
        """上传软件"""
        driver = self.driver
        driver.get(self.base_url + "/")

        # 调用登录接口
        login.login_server(driver, pyfilename, "test_1uploadPro")


        toolsdir = sys.path[0]
        # print(toolsdir)
        toolsfile = toolsdir + "\\tools\\Upload.exe"
        if not os.path.exists(toolsfile):
            # print(toolsfile + " is not exists")
            toolsfile = os.path.abspath("../..") + "\\tools\\Upload.exe"
        # print(toolsfile)
        filedir = r"D:\test.txt"

        downloadProgram(driver)

        # driver.find_element_by_id("btnE00").click() # 策略
        # driver.find_element_by_id("ext-gen1194").click() # 策略基础
        # driver.find_element_by_id("downloadProgramManageId-btnWrap").click() # 下载程序管理
        driver.find_element_by_xpath("//*[@id='addSoftwareId-btnEl']").click() # 添加软件
        driver.find_element_by_id("fileAliasNameId-inputEl").send_keys("自动化 cody.guo 测试软件")

        # 调用上传
        subprocess.Popen([toolsfile,'打开', filedir, '3000'])
        driver.find_element_by_xpath("//*[@id='uploadfileId-buttonEl']").click() # 点击浏览
        driver.find_element_by_id("softwareDescId-inputEl").send_keys("自动化 cody.guo 测试备注.")
        """
        button-1131-btnInnerEl
        button-1136-btnInnerEl
        button-1141-btnInnerEl
        """
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='uploadSoftwareWindowId']/div[3]/div/div/div[1]").click()
        # driver.find_element_by_xpath(".//*[@id='button-1131']").click()
        time.sleep(3)
        returnUpload = driver.find_element_by_xpath(".//*[@id='messagebox-1001-displayfield-inputEl']").text
        if "软件上传成功" in returnUpload:
            driver.find_element_by_xpath(".//*[@id='button-1005-btnEl']").click()
            logging.info(str(pyfilename) + "-->" + "test_1uploadPro" + "--> " + str(returnUpload))
        else:
            logging.error(str(pyfilename) + "-->" + "test_1uploadPro" + "--> " + str(returnUpload))
        # print("#" * 30 + "下载程序管理,上传软件结束." + "#" * 30)
    


    def test_2edit_program(self):
        """修改信息"""
        driver = self.driver
        driver.get(self.base_url + "/")

        # 调用登录接口
        login.login_server(driver, pyfilename, "test_2edit_program")

        downloadProgram(driver)

        # driver.find_element_by_id("btnE00").click() # 策略
        # driver.find_element_by_id("ext-gen1194").click() # 策略基础
        # driver.find_element_by_id("downloadProgramManageId-btnWrap").click() # 下载程序管理
        driver.find_element_by_xpath("//div[@id='softwareManageId-body']/div/table/tbody/tr[2]").click() # 选择第一行软件

        driver.find_element_by_id("editSoftwareId-btnIconEl").click() # 修改信息
        driver.find_element_by_id("editSoftwareNameId-inputEl").clear()
        driver.find_element_by_id("editSoftwareNameId-inputEl").send_keys("自动化 cody.guo 修改信息")
        driver.find_element_by_id("editSoftwareDescId-inputEl").clear()
        driver.find_element_by_id("editSoftwareDescId-inputEl").send_keys("自动化 cody.guo 修改信息 备注")

        driver.find_element_by_xpath("//div[@id='editSoftwareWindowId']/div[3]/div/div/div").click()

        logging.info(str(pyfilename) + "-->" + "test_2edit_program" + "--> 修改信息成功.")

    def test_3delete_program(self):
        """删除软件"""
        driver = self.driver
        driver.get(self.base_url + "/")


        # 调用登录接口
        login.login_server(driver, pyfilename, "test_3delete_program")

        downloadProgram(driver)

        # driver.find_element_by_id("btnE00").click() # 策略
        # driver.find_element_by_id("ext-gen1194").click() # 策略基础
        # driver.find_element_by_id("downloadProgramManageId-btnWrap").click() # 下载程序管理
        driver.find_element_by_xpath("//div[@id='softwareManageId-body']/div/table/tbody/tr[2]").click() # 选择第一行软件
        driver.find_element_by_id("deleteSoftwareId-btnEl").click() # 删除信息按钮

        driver.find_element_by_xpath("//*[@id='button-1006-btnEl']").click() # 确定删除
        time.sleep(2)
        
        returnDelete = driver.find_element_by_id("messagebox-1001-displayfield-inputEl").text # 获取删除结果
        if "删除成功" in returnDelete:
            
            logging.info(str(pyfilename) + "-->" + "test_3delete_program" + "--> " + str(returnDelete))
        else:
            logging.error(str(pyfilename) + "-->" + "test_3delete_program" + "--> " + str(returnDelete))

        time.sleep(2)
        driver.find_element_by_id("button-1005").click() # 删除成功确定

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # print(pyfilename)
    debug.debug(pyfilename)
    unittest.main()
