#!/usr/bin/env python
# coding:utf-8
# author: cody.guo

import requests
import urllib
import time
from hashlib import md5
from selenium import webdriver
from PIL import ImageGrab

class RClient(object):

    def __init__(self, username, password, soft_id, soft_key):
        self.username = username
        self.password = md5(password.encode("utf8")).hexdigest()
        self.soft_id = soft_id
        self.soft_key = soft_key
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    # rc = RClient('username', 'password', 'soft_id', 'soft_key')
    rc = RClient('zhuyunxia', 'zhuyunxia3427', '1', 'b40ffbee5c1cf4e38028c197eb2fc751')
    # 获取图片
    browser = webdriver.Chrome()
    # browser.get("http://reg.email.163.com/unireg/call.do?cmd=register.entrance&from=126mail") # 修改url
    browser.get("https://kyfw.12306.cn/otn/login/init") # 修改url
    browser.maximize_window()
    time.sleep(1)
    # imgurl = browser.find_element_by_id("mVcodeImg").location
    # size = browser.find_element_by_id("mVcodeImg").size
    size = browser.find_element_by_xpath("//*[@id='loginForm']/div/ul[2]/li[4]/div/div/div[3]/img").size
    imgurl = browser.find_element_by_xpath("//*[@id='loginForm']/div/ul[2]/li[4]/div/div/div[3]/img").location

    # print("size" + str(size))
    # print("imgurl" + str(imgurl))
    time.sleep(1)
    warningheight = 60 # Chrome浏览器到body之间的距离,不同浏览器不一样,需要重新计算
    gbox = (int(imgurl["x"]), imgurl["y"] + warningheight, int(imgurl["x"]) + size["width"], imgurl["y"] + size["height"] + warningheight)
    img = ImageGrab.grab(gbox)
    img.save("cody.png")

    name = "cody.png"
    im = open(name, 'rb').read()
    returncode = rc.rk_create(im, '6113')['Result'] # 修改代码6113是 http://www.ruokuai.com/home/pricetype
    print(returncode)
    # browser.find_element_by_id("mVcodeIpt").send_keys(returncode)
    
    # browser.quit()





