# coding=utf-8
# 把test_case 目录添加到path 下，这里用的相对路径
import sys
sys.path.append(sys.path[0] + "\home")
sys.path.append(sys.path[0] + "\login")
from home import *
from login import *



# 用例文件列表
def caselist():
	alltestnames = [
		iman_login_server.Login,
		#iman_tmp_case.Test_case,
		]
	print("success read case list!!")
	return alltestnames