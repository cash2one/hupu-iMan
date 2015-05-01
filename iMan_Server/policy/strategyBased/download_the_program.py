# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import time
import os
import sys
from selenium.webdriver.common.keys import Keys
sys.path.append(sys.path[0] + "\login")
from login import login
import subprocess

def downloadPro(self, url, status="login"):
    """下载程序管理"""



    # 根据状态决定是否需要重新打开浏览器登录,只有当status为login时才会调用登录服务器模块.
    if status == "login":
        # 需要传入两个参数,self 是浏览器, url 是访问地址.
        login.loginServer(self, url)

    print("#" * 30 + "下载程序管理,上传软件开始." + "#" * 30)

    uploaddir = os.getcwd()
    toolsdir = uploaddir + "\\tools\\upload.exe"
    #filedir = r"d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
    filedir = r"D:\test.txt"
    

    self.find_element_by_id("btnE00").click() # 策略
    self.find_element_by_xpath("//*[@id='ext-gen1170']/td[1]/div").click() # 策略基础
    self.find_element_by_id("downloadProgramManageId-btnWrap").click() # 下载程序管理
    self.find_element_by_xpath("//*[@id='addSoftwareId-btnEl']").click() # 添加软件
    self.find_element_by_id("fileAliasNameId-inputEl").send_keys("自动化 cody.guo 测试软件")
    subprocess.Popen([toolsdir,'2', filedir])
    self.find_element_by_xpath("//*[@id='uploadfileId-buttonEl']").click() # 点击浏览
    self.find_element_by_id("softwareDescId-inputEl").send_keys("自动化 cody.guo 测试备注.")
    """
    button-1131-btnInnerEl
    button-1136-btnInnerEl
    button-1141-btnInnerEl
    """
    time.sleep(10)
    self.find_element_by_xpath(".//*[@id='button-1131']").click()
    time.sleep(3)
    returnUpload = self.find_element_by_xpath(".//*[@id='messagebox-1001-displayfield-inputEl']").text
    print(returnUpload)
    self.find_element_by_xpath(".//*[@id='button-1005-btnEl']").click()
    print("#" * 30 + "下载程序管理,上传软件结束." + "#" * 30)


