# -*- coding: UTF-8 -*-
# author: cody.guo
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.implicitly_wait(30)

browser.find_element_by_id("kw").send_keys("s")
time.sleep(1)

ullist = browser.find_elements_by_xpath(".//*[@id='form']/div/ul") # 定位输入关键字后自动出现的ul
# 遍历ul中所有的li
for ul in ullist:
	# 如果想查询的内容在li中,ul.text获取ul内容
	if "顺丰" in ul.text:
		# 移动鼠标到指定的行,并执行确定动作
		ActionChains(browser).move_to_element(ul).click().perform()

time.sleep(5)

browser.quit()