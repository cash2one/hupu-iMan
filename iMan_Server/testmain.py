# -*- coding=UTF-8 -*-
import unittest
import sys, os
import subprocess
sys.path.append(sys.path[0] + "\home")
sys.path.append(sys.path[0] + "\policy")
#import allcase_list
# import HTMLTestRunner
from selenium import webdriver
from selenium import selenium
import winreg
import urllib.request
import logging
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




# 设置验证码识别工具的环境变量.
# env = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,\
# 	                    r"SYSTEM\ControlSet001\Control\Session Manager\Environment", \
#                         0, winreg.KEY_SET_VALUE|winreg.KEY_READ) 
# winreg.SetValueEx(env ,"TESSDATA_PREFIX", 0, winreg.REG_SZ, sys.path[0]  + r"/tools/Tesseract-OCR") 

# 打开通讯debug
logging.basicConfig(level=logging.DEBUG,
	                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',)

# 指定浏览器位置运行
firefoxBin = os.path.abspath(r"C:\Users\cody.guo\AppData\Roaming\Mozilla\Firefox\Profiles\8pfctx70.default")
os.environ["webdriver.firefox.bin"] = firefoxBin



browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.FIREFOX)
browser.implicitly_wait(30)
browser.get("http://10.10.3.227/admin")
time.sleep(2)
browser.find_element_by_id("tr1").click()

# 获取控制器的验证码
tmp = browser.find_element_by_id("randField").get_attribute("value")
print("#" * 30 + "本次的验证码为: " + tmp + "#" * 30)


# toolsdir = sys.path[0] + r"\tools\Tesseract-OCR\tesseract.exe"
# filedir = sys.path[0] + "\\tools\\Tesseract-OCR\\image2.jpg"

#subprocess.Popen([toolsdir, filedir, "2015"])

