# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 18:27
# file:spider6.py

import re #正则表达式，进行文字匹配
from bs4 import BeautifulSoup #网页解析，获取数据
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行Excel操作
import sqlite3 #进行sqlite数据

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata(baseurl) #1，爬取网页；
    savepath = ".\\豆瓣电影top250.xls"
    askurl("https://movie.douban.com/top250?start=")
def getdata(baseurl):
    datalist = []  # 2，逐一解析数据；
    for i in range(0,1): #调用获取页面信息的函数，1次； 这里1改成10，就是循环10页，250个电影
        url = baseurl + str(i*25)
        html = askurl(url) #保存获取到的网页源码；
    return datalist

def askurl(url):
    head ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36"
    } #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，我们可以接收什么水平的文件内容； #模拟浏览器头部信息，向豆瓣服务器发送消息；
    request = urllib.request.Request(url,headers=head)
    html = " "
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
def savedata(savepath):
    print("save...")
if __name__ == "__main__":#当程序执行时，调用函数
    main()