# -*- coding=UTF-8 -*-
# author: cody.guo
import os
import sys
import time
import logging



def debug(self):
	""" 定义debug输出格式 """
	nowtime = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	LOGDIR = sys.path[0] + "\\log"
	if not os.path.exists(LOGDIR):
		LOGDIR = os.path.abspath("..") + "\\log"
	if not os.path.exists(LOGDIR):
		LOGDIR = os.path.abspath("..\..") + "\\log"
	# if not os.path.exists(FILE):
	# 	FILE = os.path.abspath("..\..\..") + "\\log"
	
	LOGFILE = nowtime + "_" + str(self) + '_log.log'
	logging.basicConfig(level=logging.DEBUG,
						format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
						datefmt='%a, %d %b %Y %H:%M:%S',
						filename= os.path.join(LOGDIR, LOGFILE),
						filemode='w')
	fileLog = logging.FileHandler(os.path.join(LOGDIR, LOGFILE))
	fileLog.setLevel(logging.DEBUG)
	logging.getLogger('').addHandler(fileLog)


	# 定义一个Handler打印INFO及以上级别的日志到sys.stderr  
	console = logging.StreamHandler()  
	console.setLevel(logging.INFO)


	# 设置日志打印格式
	formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')  
	console.setFormatter(formatter)  
	# 将定义好的console日志handler添加到root logger  
	logging.getLogger('').addHandler(console)
	logging.getLogger('myloger').addHandler(console)


# debug()