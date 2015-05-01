# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import re

class ParserHTML():
	def __init__(self,value):
		self.value = value
	def __getattr__(self, name):
		print( name )
		regx = re.compile(r'<' + name + r'.*?>.*</' + name + r'>')
		return re.findall(regx, self.value)

reg = ParserHTML("html")
print( reg.li )



# import HTMLParser

# import urllib

# def getImage(addr):

# 	u = urllib.urlopen(addr)

# 	data = u.read()

# 	class parseImages(HTMLParser.HTMLParser):

# 		def handle_starttag(self, tag, attrs):

# 			if tag == 'img':

# 				for name,value in attrs:

# 					if name == 'src':

# 						getImage(urlString + "/" + value)

# 						u = urllib.urlopen(urlString)

# 						lParser.feed(u.read())



# getImage("http://10.10.3.227/cloudUser/login.jsp?ifVisit=6BE503AD2EB41B6333AD5E465EBC5489")











# #!/usr/bin/python 
# import urllib, HTMLParser 
# page_url = '' 
# #get the url raw content 
# page_src_content = urllib.urlopen(page_url) 
# page_list = list(page_src_content) 
# def page_find(LST_NAME, LST_KEYWD, STRT_ELEMT = 0): 
# 	POS_ELEMT = -1 
# 	for i in range(STRT_ELEMT,len(LST_NAME)): 
# 		if LST_NAME[i].find(LST_KEYWD) >= 0: 
# 			POS_ELEMT = i 
# 			break 
# 			return POS_ELEMT 
# 			#get the line number matchs keywords 
# 			keywd_line = page_find(page_list, 'changes files:\n') 
# 			#print keywd_line #get the end line number of the match keywords 
# 			end_line = page_list[keywd_line:].index('\n') 
# 			#print end_line 
# 			for i in range (keywd_line, keywd_line + end_line - 1): 
# 				print(page_list[i])








# import winreg
# env = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,\
# 	                    r"SYSTEM\ControlSet001\Control\Session Manager\Environment", \
#                         0, winreg.KEY_SET_VALUE|winreg.KEY_READ) 
# winreg.SetValueEx(env,"TESSDATA_PREFIX",0,winreg.REG_SZ, r"E:\cody\hupu-iMan\tools\Tesseract-OCR") 


# os.system(r"tesseract.exe E:\cody\hupu-iMan\tools\Tesseract-OCR\2015-2.png 2015-2")
# print("hello world")
# print("中文")
# def login(self, url):
#     self.get(url)
#     print(str(self) +"||"+ str(url))

# modelist = [["//input[@id='radiofield-1047-inputEl']", "//button[@id='button-1053-btnEl']"],
#             ["//input[@id='radiofield-1074-inputEl']", "//button[@id='button-1079-btnEl']"],
#             ["//input[@id='radiofield-1099-inputEl']", "//button[@id='button-1103-btnEl']"]
#             ]


# for i in range(0, 3):
# 	print(modelist[i][0] + " : " + modelist[i][1])