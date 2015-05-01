# -*- coding:utf-8 -*-
import urllib.request
url = "http://k.imgepic.net/pic/051322/hm2nhsmh0gbhm2nhsmh0gb.jpg"
name ="D:\\tmp.jpg"
# 加上浏览器头部
"""
分析:
之所以出现上面的异常,是因为如果用 urllib.request.urlopen 方式打开一个URL,
服务器端只会收到一个单纯的对于该页面访问的请求,但是服务器并不知道发送这个
请求使用的浏览器,操作系统,硬件平台等信息,而缺失这些信息的请求往往都是非正
常的访问,例如爬虫.有些网站为了防止这种非正常的访问,会验证请求信息中的UserAgent
(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),如果UserAgent存在异常
或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)所以可以尝试在请求中加入
UserAgent的信息
方案:
对于Python 3.x来说,在请求中添加UserAgent的信息非常简单,代码如下
[python]  
#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误  
#主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问
User-Agent,具体的信息可以通过火狐的FireBug插件查询  
"""
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
req = urllib.request.Request(url=url, headers=headers)  
conn = urllib.request.urlopen(req)

#保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片

# conn = urllib.request.urlopen(url)
jgpfile = open(name,'wb')
jgpfile.write(conn.read())
jgpfile.close()
print('Pic Saved!') 