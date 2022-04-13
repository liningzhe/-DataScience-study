# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 17:20
# file:spider1.py

import urllib.request

# urllib的使用

'''
#urllib.request，打开和读取URL；
# urllib.error，异常模块处理，包含urllib.request抛出的异常；
# urllib.parse，解析URL；
# url.robotparser,解析robots.txt文件；
'''

'''
#获取一个get请求;
response = urllib.request.urlopen("https://www.baidu.com/")
print(response.read()) # 出现的源代码可能比较混乱；
print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码，有利于代码显示；

# 获取一个post请求; http://httpbin.org/ 测试网站；
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data= data)
print(response.read().decode('utf-8'))
response = urllib.request.urlopen("http://httpbin.org/get",timeout=9)
print(response.read().decode('utf-8'))
'''

'''
# 模拟浏览器，超时情况下；有的页面会因为timeout，不能爬虫，所以设置异常捕获；
import urllib.error
import urllib.parse
import socket
import urllib.request
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01) #后缀为get,设置时间0.01s，会出现报错；
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('timeout')
'''

'''
response = urllib.request.urlopen("http://douban.com")
print(response.status) # 状态码，判断请求是否成功；418是发现你是爬虫；404是找不到，等等；
response = urllib.request.urlopen("http://www.baidu.com")
print(response.getheaders())   #响应头，得到一个元组组成的列表；读取网页全部的内容；
print(response.getheader('Server')) #得到特定的响应头；读取具体内容；
print(response.read().decode("utf-8")) #获取响应体的内容，字节流的数据；需要转utf-8
'''

'''
from urllib import request,parse
# 分别创建字符串，字典等来带入到request对象里面；
url = "http://httpbin.org/post"
headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"}
dict ={
    'name':'jay'
}
data = bytes(parse.urlencode({"name":"eric"}),encoding="utf-8")
req = request.Request(url=url,data=data,headers=headers,method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))
'''

'''
from urllib import request,parse
# 通过addheaders方法不断的向原始的request对象里不断添加；
url = "http://httpbin.org/post"
dict = {
    'name':'cq'
}
data = bytes(parse.urlencode(dict),encoding="utf-8")
req = request.Request(url=url,data=data,method="POST")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36")
response = request.urlopen(req)
print(response.read().decode("utf-8"))
'''

'''
# 打印出信息cookies
import http.cookiejar,urllib.request
cookie = http.cookiejar.CookieJar()
handerler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handerler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)
'''

#保存cookie文件，两种格式；
'''
#第一种格式
import http.cookiejar,urllib.request
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handerler =urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handerler)
response =opener.open('http://www.baidu.com') #获取response后cookie会自动赋值；
cookie.save(ignore_discard=True,ignore_expires=True)
# 第二种格式
import http.cookiejar,urllib.request
filename = 'cookie2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handerler =urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handerler)
response =opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''
# 用文本文件的形式维持登录状态
'''
import http.cookiejar,urllib.request
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie2.txt',ignore_discard=True,ignore_expires=True)
handerler =urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handerler)
response =opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
'''

# import urllib.request
# url= urllib.request.urlopen("https://www.naver.com/")
# print(url.getcode()) #getcode（）函数，获取网页状态；200表示正常；404表示网页不存在；不能绝对相信状态码，要看能不能得到数据；

# 异常处理部分，需要了解有httperror和URLerror两种，父类与子类的关系
#父类，只有一个原因
# from urllib import request,error
# try:
#     response =request.urlopen('http://www.baidu.com/index.html')
# except error.URLError as e:
#     print(e.reason)

#子类，有更多的属性
# from urllib import request,error
# try:
#     response =request.urlopen('http://abc.123/index.html')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')

# 解析，将一个url解析
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#commnt')
print(result)
print(type(result))
result = urlparse('http://www.baidu.com/index.html;user?id=5#commnt',scheme='https')
print(result)
result = urlparse('http://www.baidu.com/index.html;user?id=5#commnt',allow_fragments=False) #结果被拼接；
print(result)
result = urlparse('http://www.baidu.com/index.html#commnt',allow_fragments=False) #会被拼接到path；
print(result)
# 拼接URL
from urllib.parse import urlunparse
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))
# 字典方式直接转换成url参数
from urllib.parse import urlencode
params ={
    'name':'germey',
    'age':'122'
}
base_url= 'http://www.baidu.com?'
url = base_url+urlencode(params)
print(url)