# -*- coding=UTF-8 -*-
import unittest
import sys
import subprocess
sys.path.append(sys.path[0] + "\home")
sys.path.append(sys.path[0] + "\policy")
from home import import_license
from home import apply_for_authorisation
from policy.strategyBased import download_the_program
#import allcase_list
# import HTMLTestRunner
from selenium import webdriver
from selenium import selenium
import winreg




# 设置验证码识别工具的环境变量.
env = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,\
	                    r"SYSTEM\ControlSet001\Control\Session Manager\Environment", \
                        0, winreg.KEY_SET_VALUE|winreg.KEY_READ) 
winreg.SetValueEx(env ,"TESSDATA_PREFIX", 0, winreg.REG_SZ, sys.path[0]  + r"\tools\Tesseract-OCR") 


toolsdir = sys.path[0] + "\\tools\\Tesseract-OCR\\tesseract.exe"
filedir = "http://test.bigaka.com/randNum.do"
# filedir = sys.path[0] + "\\tools\\Tesseract-OCR\\image2.jpg"
subprocess.Popen([toolsdir, filedir, "2015-cody"])


# browser = webdriver.Chrome()
# browser.get("http://10.10.3.228/admin")

# browser.find_element_by_id("tr1").click()
# tmp  = selenium.selenium.get_Value("//input[@id='randField']")

# print(tmp)


# alltestnames = allcase_list.caselist()

# # 创建测试套件
# testunit = unittest.TestSuite()


# 测试
def caseTest():
	#apply_for_authorisation.appForauthor(browser, "http://10.10.3.227/admin", status="login")
	#import_license.impLicense(browser, "http://10.10.3.227/admin", status="login")
	download_the_program.downloadPro(browser, "http://10.10.3.227/admin", status="login")
	browser.quit()

# browser = webdriver.Firefox()
# browser.maximize_window()
# print("-" * 30 + "火狐浏览器" + "-" * 30)
# caseTest()

# browser = webdriver.Chrome()
# browser.maximize_window()
# print("-" * 50 + "谷歌浏览器" + "-" * 50)
# caseTest()

# browser = webdriver.Ie()
# caseTest()





#import_license.import_lic(fireBrowser, "http://10.10.3.227/admin")

# testunit.addTest(unittest.makeSuite(import_license.apply_for(fireBrowser, "http://10.10.3.227/admin")))
# testunit.addTest(unittest.makeSuite(import_lic(fireBrowser, "http://10.10.3.227/admin")))

# runner = unittest.TextTestRunner()
# runner.run(testunit)
# for test in alltestnames:
# 	testunit.addTest(unittest.makeSuite(test))

# filename = "D:\\tmp.html"

# fp = file(filename, 'wb')
# runner =HTMLTestRunner.HTMLTestRunner(
# 	stream=fp,
# 	title=u'百度搜索测试报告',
# 	description=u'用例执行情况：')


# fireBrowser = webdriver.Firefox()
# login.login(fireBrowser, "http://10.10.3.227/admin")

