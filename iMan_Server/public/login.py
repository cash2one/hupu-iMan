# -*- coding=UTF-8 -*-
__author__ = 'cody.guo'
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



def login_server(self):
    """登录服务器"""
    # 打开要访问的服务器地址
    print("#" * 30 + "开始访问并登录服务器." + "#" * 30)

    # 选择登录服务器
    self.find_element_by_id("tr0").click()

    # 智能等待并输入用户名、密码、公司编码
    self.find_element_by_id("accountId").send_keys("admin")  #输入用户名
    self.find_element_by_id("passwordId").send_keys("admin") #输入密码
    self.find_element_by_id("companycodeId").send_keys("10000000")  #输入公司编码

    # 点击登录按钮
    self.find_element_by_xpath("//input[@type='submit']").click()

    # # 获取当前登录管理员,是否使用admin登录,错误退出.
    name = self.find_element_by_xpath(".//*[@id='panel-1012-body']/div[1]").text
    assert name != "admin", name + " 登录错误账号."

    print("#" * 30 + "登录服务器结束." + "#" * 30)
