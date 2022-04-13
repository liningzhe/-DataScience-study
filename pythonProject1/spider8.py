# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 20:38
# file:spider8.py

# 保存到数据库的操作，之前是保存到Excel；主要是建表的过程，中间 getdata，askURL，savedata和spider7一样；

import re #正则表达式，进行文字匹配
from bs4 import BeautifulSoup #网页解析，获取数据
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行Excel操作
import sqlite3 #进行sqlite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
#     # 1，爬取网页；
    datalist = getdata(baseurl)
    dbpath = 'movie.db'
#     # 2,保存数据；
    saveData2DB(datalist,dbpath)

findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）# 影片详情的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中；#影片图片的规则
findtitle = re.compile(r'<span class="title">(.*)</span>')  # 影片片名；
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 影片评分的规则；
findjudge = re.compile(r'<span>(\d*)人评价</span>')  # 影片评价人数的规则；
findinq = re.compile(r'<span class="inq">(.*)</span>')  # 影片概况的规则；
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 影片的内容的规则；


def getdata(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askurl(url)  # 保存获取到的网页源码；
        # 2，逐一解析数据；
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符号要求的字符串，形成列表；
            # print(item) #这是为了测试，写了这行，查看电影item全部信息；
            data = []  # 保存一部电影的所有信息；
            item = str(item)

            link = re.findall(findlink, item)[0]  # re库用来用过正则表达式查找指定的字符串；
            data.append(link)

            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc)

            titles = re.findall(findtitle, item)  # 有可能只有一个中文名；
            if (len(titles) == 2):
                ctitle = titles[0]  # 添加中文名；
                data.append(ctitle)
                otitle = titles[1].replace('/', ' ')  # .replace()去掉外文名字前无关的符号；添加外文名；
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')  # 如果只有一个中文名，外文名留空；

            rating = re.findall(findrating, item)[0]
            data.append(rating)

            judge = re.findall(findjudge, item)[0]
            data.append(judge)

            inq = re.findall(findinq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", " ")  # 去掉不需要的句号； #源码中外文名后&nbsp，演员介绍部分有&nbsp源码，所以表里有；
                data.append(inq)  # 添加概述；
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br/(\s+)?/>(\s+)?', " ", bd)  # 去掉不需要的br； 这步骤，我失败，依然有br；老师没有；
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格；

            datalist.append(data)  # 把处理好的一部电影信息放入datalist；
    # print(datalist)  #这个地方 我有问题；老师删出这行，可以操作；我是删除，不能操作；
    return datalist


def askurl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36"
    }  # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，我们可以接收什么水平的文件内容； #模拟浏览器头部信息，向豆瓣服务器发送消息；
    request = urllib.request.Request(url, headers=head)
    html = " "
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def savedata(datelist, savepath):  # 保存数据
    print("save...")

    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象；
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)  # 创建工作表；
    col = ('电影详情链接', "图片链接", "影片中文名", "影片外文名", "评分", "评价人数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datelist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存数据表；

def saveData2DB(datalist,dbpath):
    print('...')
def init_db(dbpath):
    sql ='''create table movie250
            (id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            instroduction text,
            info text
            ); '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__== '__main__':
    init_db('movietest.db') #没有这个movietest.db文件，这样可以进行创建；
    print('爬取完毕')