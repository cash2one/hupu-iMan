#coding=utf-8
import unittest
import sys
import time
import os
import datetime
import HTMLTestRunner
import allcase_list
from tools import send_mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

alltestnames = allcase_list.caselist()

testunit = unittest.TestSuite()

for tmplist in alltestnames:
	testunit.addTest(unittest.makeSuite(tmplist))


# 取前面时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

filename = sys.path[0] + "\\result\\" + now + 'result.html'
result_file = open(filename, "wb")


runner = HTMLTestRunner.HTMLTestRunner(
        stream=result_file,
        title=u"互普iMan-Server自动化测试用例",
        description=u"执行测试用例报告.")

if __name__ == "__main__":
	#执行测试用例
	run_status = runner.run(testunit)
	result_file.close()
	time.sleep(6)
	#执行发邮件
	send_mail.send_result_mail()
