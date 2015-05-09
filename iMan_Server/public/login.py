# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import sys
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def login_server(self, pyfilename, testname):
    """登录服务器"""
    # print("#" * 30 + "开始访问并登录服务器." + "#" * 30)
    # 选择 服务器
    self.find_element_by_xpath("//*[@id='tr0']/div/img").click()

    # 输入用户名、密码、公司编码
    self.find_element_by_id("accountId").send_keys("admin")  #输入用户名
    self.find_element_by_id("passwordId").send_keys("admin") #输入密码
    self.find_element_by_id("companycodeId").send_keys("10000000")  #输入公司编码

    # 点击登录按钮
    self.find_element_by_xpath("//input[@type='submit']").click()

    # 获取当前登录管理员,是否使用admin登录,错误退出.
    name = self.find_element_by_xpath("//*[@id='panel-1012-body']/div[1]").text
    assert name != "admin", name + " 登录错误账号."

    # print("#" * 30 + "登录服务器结束." + "#" * 30)
    logging.info(str(pyfilename) + "-->" + str(testname) +  "--> 登录服务器成功.")


# if __name__ == "__main__":
#     browser = webdriver.Chrome()
#     browser.get("http://10.10.3.227/admin")
#     browser.implicitly_wait(30)
#     login(browser)