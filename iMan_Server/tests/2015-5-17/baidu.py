# -*- coding: UTF-8 -*-
# author: cody.guo
import time
from selenium import webdriver



browser = webdriver.PhantomJS()
browser.get("https://www.baidu.com")
browser.implicitly_wait(30)

print(browser.title)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(1)
print(browser.title)
browser.quit()