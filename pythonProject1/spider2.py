# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 17:35
# file:spider2.py

import re #正则表达式，进行文字匹配
from bs4 import BeautifulSoup #网页解析，获取数据
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行Excel操作
import sqlite3 #进行sqlite数据库操作
#正则表达式
'''
import re
line = "Cats are smarter than dogs" # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# 用()表示一个组，2个组；group：获取子模式(组)的匹配项；
# 建议在正则表达式中，被比较的字符串前加上r，这样不用担心转义字符的问题；
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

print(matchObj.start(2)) #组2开始的索引
print(matchObj.end(2)) #组2结束的索引；
print(matchObj.span(2) #组2开始，结束的索引；
'''
#  第一种情况，有pattern对象；
'''
# compile()函数的定义: 将正则表达式编译成 Pattern对象, 即创建模式对象
re.compile(pattern[, flag])
pattern 是一个字符串形式的正则表达式，flag 是一个可选参数，表示匹配模式，比如忽略大小写，多行模式等。
pattern = re.compile(r'\d+')

# compile()，返回的是一个匹配对象，单独使用就没有任何意义，需要和findall(), search(), match(）搭配使用。 

# compile()与findall()一起使用，返回一个列表；
import re
def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')
    x = regex.findall(content)
    print(x)
if __name__ == '__main__':
    main()
# ['Hello', 'from', 'Chongqing', 'montain', 'to', 'you']

# compile()与match()一起使用，可返回一个class、str、tuple/
    但是一定需要注意match()，从位置0开始匹配，匹配不到会返回None，
    返回None的时候就没有span/group属性了，并且与group使用，返回一个单词‘Hello’后匹配就会结束。
import re
def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')
    y = regex.match(content)
    print(y)
    print(type(y))
    print(y.group())
    print(y.span())
if __name__ == '__main__':
    main()
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>
# <class '_sre.SRE_Match'>
# Hello
# (0, 5)

# compile()与search()搭配使用, 返回的类型与match()差不多，
    但是不同的是search(), 可以不从位置0开始匹配。
    但是匹配一个单词之后，匹配和match()一样，匹配就会结束。
    
pattern = re.compile("AA")
m = pattern.search("CBA")
print(m)
m = pat.search("ACBAADDCCAAA")
print(m)
'''

# 第二种情况：没有pattern对象
'''
m = re.search('asd','Aasd') #前面的字符串是规则/正则表达式（asd),后面的字符串（Aasd）是被检验的对象；
print(m)

import re
print(re.match('www', 'www.runoob.com').span())  #在起始位置匹配,re.match尝试从字符串的起始位置匹配一个模式;
print(re.match('com', 'www.runoob.com')) #不在起始位置匹配,match()就返回none;

print(re.findall('a','adddddsadda'))
print(re.findall('[A-Z]','ASSDKFzzzzzaaaX')) #找到a到z间的大写字母；
print(re.findall('[A-Z]+','ASSDKFzzzzzaaaX')) # +的定义；
# sub
print(re.sub('a','A','abcdcasd')) #找到a 用A替换，在第三个字符串中返回结果;
'''

# 正则提取；


def main():
    baseurl = "https://movie.douban.com/top250?start="
#     # 1，爬取网页；
    datalist = getdata(baseurl)
    savepath = ".\\豆瓣电影top250.xls"
# askurl("https://movie.douban.com/top250?start=")

def getdata(baseurl):
    datalist = []
    for i in range(0, 1):  # 调用获取页面信息的函数，只打印第一页；
        url = baseurl + str(i * 25)
        html = askurl(url)  # 保存获取到的网页源码；
# 2 逐一解析数据
        soup= BeautifulSoup(html,"html.parser") #"html.parser"是一种页面解析器；
        for item in soup.find_all('div', class_="item"): #每个电影都在一个<div>标签中，且每个div标签都有一个属性class=item
            # print(item) #测试：查看电影item全部信息；
            data =[] #保存一部电影的所有信息；
            item = str(item)
            print(item)
            break #打印一个电影的源码；好下一步进行超链接，图片，电影名等的解析；
    return datalist

# 得到页面全部内容；
def askurl(url):
    head ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36"
    } #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，我们可以接收什么水平的文件内容； #模拟浏览器头部信息，向豆瓣服务器发送消息；
    request = urllib.request.Request(url,headers=head)   #发送请求；
    html = " "
    try:
        response = urllib.request.urlopen(request) #去得响应；
        html = response.read().decode("utf-8") #获取网页内容；
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def savedata(datelist,savepath): #保存数据
    print("save...")
