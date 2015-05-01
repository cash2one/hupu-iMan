#coding=utf-8
import unittest
import sys
import time
import os
import datetime
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

global RESULT_FILE_NAME
RESULT_FILE_NAME = "自动化测试报告"

def sentmail(file_new):
	# 发信邮箱
	mail_from = 'iman@hupu.net'

	#收信邮箱
	mail_to = 'hp131@hupu.net'

	#定义正文
	f = open(file_new, 'rb')
	mail_body = f.read()
	print(mail_body)
	f.close()
	print(file_new)
	

	#定义标题
	msgRoot = MIMEMultipart('related')
	timec = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	msgRoot['Subject'] = u"互普iMan - 自动化测试报告" + timec
	msgRoot['From'] = '自动化测试员' + '<' + str(mail_from) + '>' 
	msgText = MIMEText(mail_body,_subtype='html',_charset='utf-8')
	msgRoot['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
	msgRoot.attach(msgText)

	att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="%s"' % (file_new)
	msgRoot.attach(att)

	#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
	
	try:
		smtp = smtplib.SMTP()

		# 连接SMTP 服务器，此处用的hupu的SMTP 服务器
		smtp.connect('smtp.hupu.net')
		# 用户名密码
		smtp.login('iman@hupu.net','hupu2014')
		smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
		smtp.close()
	except Exception as e:
		print(e)
		sys.exit(1)
		
# 查找测试报告，调用发邮件功能
def sendreport():
	result_dir = os.path.abspath("..")  + '\\result'

	lists = os.listdir(result_dir)
	lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not \
		os.path.isdir(result_dir + "\\"+ fn) else 0)

	print(u'最新测试生成的报告: ' + lists[-1])
	RESULT_FILE_NAME = str(lists[-1])
	
	#找到最新生成的文件
	file_new = os.path.join(result_dir, lists[-1])
	print(file_new)

	#调用发邮件模块
	sentmail(file_new)
	print('email has send out !')
	

sendreport()



# def send_email(msg,file_name):
#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = file_name#邮件标题，这里我把标题设成了你所发的附件名
#     msgText = MIMEText('%s'%msg,'html','utf-8')#你所发的文字信息将以html形式呈现
#     msgRoot.attach(msgText)
#     att = MIMEText(open('%s'%file_name, 'rb').read(), 'base64', 'utf-8')#添加附件
#     att["Content-Type"] = 'application/octet-stream'
#     att["Content-Disposition"] = 'attachment; filename="%s"'%file_name
#     msgRoot.attach(att)
#     while 1:#持续尝试发送，直到发送成功
#         try:
#             smtp.sendmail(sender, receiver, msgRoot.as_string())#发送邮件 
#             break
#         except:
#             try:
#                 smtp.connect(smtpserver)#连接至邮件服务器
#                 smtp.login(username, password)#登录邮件服务器
#             except:
#                 print "failed to login to smtp server"#登录失败
                
# if __name__ == "__main__":
#     MSG=""#要发送的文字
#     FILE=""#要发送的文件
#     send_email(MSG,FILE)