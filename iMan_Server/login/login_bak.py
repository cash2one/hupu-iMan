__author__ = 'cody.guo'
import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(self, url):
    # 打开要访问的服务器地址
    print("#" * 30 + "开始访问并登录服务器." + "#" * 30)
    self.get(url)
    print(str(self) +"||"+ str(url))
    if "Hupu-iMan" == self.title:
        print("访问互普网官 网络接入管理系统成功.")
    else:
        print("访问互普网官 网络接入管理系统失败,程序退出.")
        sys.exit()

    # 选择登陆服务器
    self.find_element_by_id("tr0").click()
    self.implicitly_wait(10)
    if "Hupu-iMan Server" == self.title:
        print("访问互普网官 网络接入管理系统·服务器成功.")
    else:
        print("访问互普网官 网络接入管理系统·服务器失败,程序退出.")
        sys.exit()

    # 智能等待并输入用户名、密码、公司编码
    self.implicitly_wait(30)
    self.find_element_by_id("accountId").send_keys("admin")  #输入用户名
    self.find_element_by_id("passwordId").send_keys("admin") #输入密码
    self.find_element_by_id("companycodeId").send_keys("10000000")  #输入公司编码

    # 点击登录按钮
    self.find_element_by_xpath("//input[@type='submit']").click()
    self.implicitly_wait(30)

    # 获取当前登录管理员
    name = self.find_element_by_xpath(".//*[@id='panel-1012-body']/div[1]").text
    if "admin" in name:
        print("管理员admin登录成功.")
    else:
        print("管理员admin登录失败.")
        sys.exit(1)
    time.sleep(3)
    #self.quit()
    print("#" * 30 + "登录服务器结束." + "#" * 30)



