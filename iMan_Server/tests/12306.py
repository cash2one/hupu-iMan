# -*- coding: UTF-8 -*-
# author: cody.guo
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get("https://kyfw.12306.cn/otn/leftTicket/init")
browser.implicitly_wait(30)

browser.find_element_by_id("date_icon_1").click()
time.sleep(1)
tmp = browser.find_element_by_xpath(".//*[@id='dpTitle']/div[4]")
ActionChains.move_to_element(tmp).click().perform()
browser.find_element_by_xpath(".//*[@id='dpTitle']/div[4]").clear()
browser.find_element_by_xpath(".//*[@id='dpTitle']/div[4]").send_keys("2013")
# browser.find_element_by_xpath(".//*[@id='dpTitle']/div[4]/input").clear()
# browser.find_element_by_xpath(".//*[@id='dpTitle']/div[4]/input").send_keys("2013")
# browser.find_element_by_xpath(".//*[@id='dpTitle']/div[3]/input").clear()
# browser.find_element_by_xpath(".//*[@id='dpTitle']/div[3]/input").send_keys("3")

tmp = browser.find_elements_by_xpath("html/body/div/div[3]/table/tbody")

for i in tmp:
	print(i.text)

