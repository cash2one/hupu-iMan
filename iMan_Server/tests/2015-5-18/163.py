# -*- coding: UTF-8 -*-
# author: cody.guo

from selenium import webdriver



browser = webdriver.Chrome()

browser.get("http://reg.email.163.com/unireg/call.do?cmd=register.entrance")

browser.find_element_by_id("mobileIpt").send_keys("18821201646")
browser.implicitly_wait(30)
imgurl = browser.find_element_by_id("mVcodeImg").get_attribute("src")
print(imgurl)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
req = urllib.request.Request(url=url, headers=headers)  
conn = urllib.request.urlopen(req)

jgpfile = open("name",'wb')
jgpfile.write(conn.read())
jgpfile.close()

browser.quit()