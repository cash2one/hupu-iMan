# -*- coding=UTF-8 -*-
# author: cody.guo

import sys
sys.path.append(sys.path[0] + "\home")
sys.path.append(sys.path[0] + "\login")
sys.path.append(sys.path[0] + "\policy")
sys.path.append(sys.path[0] + "\policy\strategyBased")
from home import *
from login import *
from strategyBased import iman_download_the_program



# 用例文件列表
def caselist():
	alltestnames = [
		iman_login_server.Login,
		iman_license.Test_license,
		iman_download_the_program.Test_download_program,
		]
	print("success read case list!!")
	return alltestnames