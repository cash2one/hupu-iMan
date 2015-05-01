# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import time
import os
import sys
from selenium.webdriver.common.keys import Keys
sys.path.append(sys.path[0] + "\login")
from login import login
import subprocess


def impLicense(self, url, status="login"):
    """导入授权"""

	# 根据状态决定是否需要重新打开浏览器登录,只有当status为login时才会调用登录服务器模块.
    if status == "login":
        # 需要传入两个参数,self 是浏览器, url 是访问地址.
        login.loginServer(self, url)
        # 由于按钮ID会变化，所以根据是否调用login来定位不同的ID
        import_buttonE1 = "button-1037-btnEl"  # 导入按钮
        sure_buttonE1 = "button-1005-btnEl"    # 确定按钮
    else:
        import_buttonE1 = "button-1111-btnEl"  # 导入按钮
        sure_buttonE1 = "button-1005-btnEl"    # 确定按钮

    print("#" * 30 + "导入授权开始" + "#" * 30)

    uploaddir = os.getcwd()
    toolsdir = uploaddir + "\\tools\\upload.exe"
    #filedir = r"d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
    filedir = r"D:\test.txt"
    subprocess.Popen([toolsdir,'2', filedir])

    self.find_element_by_xpath(".//*[@id='accreditInfo']/table/tbody/tr[2]/td[3]/a").click()
    time.sleep(1)
    print("正在定位....")
    #self.find_element_by_xpath(".//*[@id='upLicenseId-browseButtonWrap']/div/em/button").click()
    self.find_element_by_xpath("//*[@id='upLicenseId-buttonEl']").click()
    time.sleep(12)


    self.find_element_by_id(import_buttonE1).click()
    time.sleep(3)

    messagebox = self.find_element_by_xpath("//div[@id='messagebox-1001-displayfield-inputEl']").text
    if "该License文件已经使用过或正在使用" in messagebox:
        print("该License文件已经使用过或正在使用.")
        #self.close()
    elif "文件导入失败" in messagebox:
        print("文件导入失败,文件格式不正确.")
        #self.close()
    else:
    	print(messagebox)
    #print(sure_buttonE1)
    self.find_element_by_id(sure_buttonE1).click()
    
    print("#" * 30 + "导入授权结束" + "#" * 30)
