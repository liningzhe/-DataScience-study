# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 21:52
# file:spider9.py

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
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 影片片名；
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 影片评分的规则；
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 影片评价人数的规则；
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 影片概况的规则；
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

            #影片详情的超链接；
            link = re.findall(findlink, item)[0]  # re库用来用过正则表达式查找指定的字符串；
            data.append(link) #添加链接
            #影片的海报；
            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc) #添加海报
            #影片的名字；
            titles = re.findall(findTitle, item)  # 有可能只有一个中文名；
            if (len(titles) == 2):
                ctitle = titles[0]  # 添加中文名；
                data.append(ctitle)
                otitle = titles[1].replace("/","")  # .replace()去掉外文名字前无关的符号；
                data.append(otitle) #添加外文名；
            else:
                data.append(titles[0])
                data.append(' ')  # 如果只有一个中文名，外文名留空；以后要放到表格里，所以没有名字，也要留空占位；
            #影片的评分；
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            #影片的评价人数；
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            # 影片的概述；
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")  # 去掉不需要的句号；
                data.append(inq)  # 添加概述；
            else:
                data.append(" ")  # 留空
            # 影片的演员人员什么；
            bd = re.findall(findBd, item)[0]
            # bd = re.sub(remove," ",bd)
            bd = re.sub('<br/(\s+)?/>(\s+)?'," ",bd)  # 去掉不需要的br； 这步骤，我失败，依然有br；老师没有；
            bd = re.sub('/'," ",bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格；

            datalist.append(data)  # 把处理好的一部电影信息放入datalist；
    print(datalist)  #这个地方 我有问题；老师删出这行，可以操作；我是删除，不能操作；
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


def savedata(datelist, savepath):  # 保存数据 datalist是封装好的数据，dbpath是数据库文件存放的全路径；
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
    init_db(dbpath)    #创建数据表
    conn =sqlite3.connect(dbpath) #连接数据库
    cur = conn.cursor() #获取游标
    for data in datalist: #对每行数据进行操作
        for index in range(len(data)): #index是每行数据的下标；
            if index == 4 or index ==5:
                continue  #这里是因为运行打印后，发现第五，第六列是整型数，所以5,6的下标不需要加'"'
        #for index in range (len(data)):
            #datac[index]=("\""+data[index]+"\"")
            data[index]=("\""+data[index]+"\"")
        sql ='''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s) '''%" ,".join(data)
        print(sql)
        cur.execute(sql) #这里打印语句，为了运行检验；如果不加print(sql),cur和commit不需要注释；
        conn.commit()
    cur.close()
    conn.close()

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

if __name__ == "__main__":#当程序执行时，调用函数
    main()
    print("爬取完毕")