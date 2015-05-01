__author__ = 'cody.guo'
import sys
import time
sys.path.append(sys.path[0] + "\login")
from login import login
from selenium.webdriver.common.keys import Keys



def appForauthor(self, url, status="login"):
    """申请授权"""

    # 调用登录
    if status == "login":
        login.loginServer(self, url)
    #"控制器" : "//input[@id='radiofield-1054-inputEl']",
    #"服务器" : "//input[@id='radiofield-1055-inputEl']"
    # 1047 1048 1049         
    # 1073 1074 1075          26
    # 1097 1098 1099          24
    # 1121 1122 1123          24
    # 1145 1146 1147          24

    modedirc = {"//input[@id='radiofield-1047-inputEl']" : "控制器",
                "//input[@id='radiofield-1074-inputEl']" : "服务器",
                "//input[@id='radiofield-1099-inputEl']" : "控制器+服务器"
                }

    modelist = [["//input[@id='radiofield-1047-inputEl']", "//button[@id='button-1053-btnEl']"],
                ["//input[@id='radiofield-1074-inputEl']", "//button[@id='button-1079-btnEl']"],
                ["//input[@id='radiofield-1099-inputEl']", "//button[@id='button-1103-btnEl']"]
               ]

    def inputreg():
        print("#" * 30 + "申请授权" + "#" * 30)
        self.find_element_by_xpath(".//*[@id='accreditInfo']/table/tbody/tr[1]/td[3]/a").click()   # 点击申请授权
        self.implicitly_wait(10)

        self.find_element_by_xpath("//input[@id='aplCompNameId-inputEl']").send_keys("自动化 cody.guo 上海互普信息技术有限公司")
        self.find_element_by_xpath("//input[@id='aplRegAddrId-inputEl']").send_keys("自动化 cody.guo 灵岩南路295号")
        self.find_element_by_xpath("//input[@id='aplContacterId-inputEl']").send_keys("自动化 cody.guo")
        self.find_element_by_xpath("//input[@id='aplPhonenumId-inputEl']").send_keys("18821201646")
        self.find_element_by_xpath("//input[@id='aplEmailId-inputEl']").send_keys("hp131@hupu.net")
        self.find_element_by_xpath("//textarea[@id='aplRemarkId-inputEl']").send_keys("自动化 cody.guo 备注信息.")


    
    for mode in range(0, 3):
        # 输入表单
        inputreg()
        #print(modelist[mode][0] + " : " + modelist[mode][1])
             
        self.find_element_by_xpath(modelist[mode][0]).send_keys(Keys.SPACE)  # 选择服务器+控制器模式
        self.find_element_by_xpath(modelist[mode][1]).send_keys(Keys.ENTER)  # 点击提交申请按钮

        # 等待2秒返回提交成功还是失败.
        time.sleep(2)
        returnote = self.find_element_by_id("messagebox-1001-displayfield-inputEl").text  # 获取返回结果
        #print(returnote)
        if "申请已提交成功" in returnote:
            print(modedirc[modelist[mode][0]] + " 授权申请成功.")
        else:
            print(modedirc[modelist[mode][0]] + "授权申请失败.")
            #self.close()
        self.find_element_by_xpath("//button[@id='button-1005-btnEl']").click()  # 点击确定按钮

    print("#" * 30 + "申请授权结束." + "#" * 30)
