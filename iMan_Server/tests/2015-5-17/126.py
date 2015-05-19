# -*- coding: UTF-8 -*-
# author: cody.guo
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.PhantomJS()
browser.get("https://www.baidu.com")

print(browser.title)



# browser.get("http://reg.email.163.com/unireg/call.do?cmd=register.entrance&from=126mail")
"""
Firefox 
    »ðºüä¯ÀÀÆ÷
"""

# browser.find_element_by_xpath("//ul[@id='tabsUl']/li[1]").click()
