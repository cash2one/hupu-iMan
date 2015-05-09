# -*- coding=UTF-8 -*-
# author: cody.guo

import os
import sys
import time
import logging
import datetime
import unittest
import all_case_list
from tools import debug
import HTMLTestRunner
from tools import send_mail
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

"""
logging.basicConfig(level=logging.DEBUG,
	                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',)
"""

# 获取测试用例集
alltestnames = all_case_list.caselist()

# 创建测试套件
testunit = unittest.TestSuite()

# 遍历添加用例集到测试套件中
for tmplist in alltestnames:
	testunit.addTest(unittest.makeSuite(tmplist))

# 取当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

# 生成测试报告
filename = sys.path[0] + "\\result\\" + now + '-result.html'
result_file = open(filename, "wb")

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
        stream=result_file,
        title=u"互普iMan-Server自动化测试报告",
        description=u"执行测试用例报告.")

if __name__ == "__main__":
	debug.debug("all_tests")
	# 执行测试用例
	run_status = runner.run(testunit)

	# 关闭测试报告写入
	result_file.close()

	# 执行发邮件
	send_mail.send_result_mail()
