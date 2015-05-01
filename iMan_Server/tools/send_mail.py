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

    

def find_result():
    result_dir = os.path.abspath("..")  + "\\result"
    if not os.path.exists(result_dir):
        result_dir = os.path.abspath(".") + "\\result"

    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not \
        os.path.isdir(result_dir + "\\"+ fn) else 0)
    print(u'最新测试生成的报告: ' + lists[-1])
    
    #找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    return file_new
    #print(file_new)

def send_result_mail():
    """发送测试报告"""
    file_new = find_result()
    # 发信邮箱
    mail_from = 'iman@hupu.net'

    #收信邮箱
    mail_to = 'hp131@hupu.net'

    #定义正文
    result_file = open(file_new, 'rb')
    mail_body = result_file.read()
    #print(mail_body)
    result_file.close()

    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')

    #定义标题
    timec = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msg['Subject'] = u"互普iMan - 自动化测试报告" + timec
    msg['From'] = '自动化测试员' + '<' + str(mail_from) + '>' 

    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    try:
        smtp = smtplib.SMTP()

        # 连接SMTP 服务器，此处用的hupu的SMTP 服务器
        smtp.connect('smtp.hupu.net')
        # 用户名密码
        smtp.login('iman@hupu.net','hupu2014')
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp.close()
        print('email has send out !')
    except Exception as e:
        print(e)
        sys.exit(1)
if __name__ == "__main__":
    send_result_mail()