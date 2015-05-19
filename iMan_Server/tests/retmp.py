# -*- coding: UTF-8 -*-
# author: cody.guo
import re
# text = r"Guido will be out of the office from 12/15/2012 - 1/3/2013."

# ip = "10.10.1.1 - 10.10.2.1 - 192.168.1.1 - 172.16.1.1 - 10.10.10.2 - 910.10.10.1"

# ippat = re.compile(r'([0-255]){1,3}\.([0-255]){1,3}\.[0-255]{1,3}?\.[1-255]{1,3}?')
# for tmp in ippat.findall(ip):
# 	print(tmp)

# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# for m in datepat.finditer(text):
# 	print(m.group())

# pattern = re.compile(r"hello")

# match1 = pattern.match('hello world.')
# match2 = pattern.match('helloo world.')
# match3 = pattern.match("helllo world.")
# if match1:
# 	print(match1.group())
# else:
# 	print("匹配失败.")
# if match2:
# 	print(match2.group())
# else:
# 	print("匹配失败.")

# if match3:
# 	print(match3.group())
# else:
# 	print("匹配失败.")

html = '<pre class="line mt-10 q-content" accuse="qContent">\
目的是通过第一次soup.find按class粗略筛选并通过soup.find_all筛选出列表中的a标签并读入href和title属性<br><br>\
但是由于目标链接可能有图片链接,而这是我不想要的.请问如何去除?<br></pre>'

reg = re.compile('<[^>]*>')

print(reg.sub('cody',html))