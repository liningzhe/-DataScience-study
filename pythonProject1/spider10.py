# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/3 0:55
# file:spider10.py
# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 21:52
# file:spider9.py

import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata(baseurl)
    dbpath = 'mymovie.db'
    saveData2DB(datalist,dbpath)

findlink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getdata(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askurl(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)


            link = re.findall(findlink, item)[0]
            data.append(link)
            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)

                otitle = titles[1].replace(" ","")
                # otitle = titles[1].replace("&nbsp;","").replace("&emsp;","").replace('\xa0/ \xa0','')
                '''
                1 > 先把字符串转码
                let data = encodeURI(要转化的值)
                2 > 接下来替换掉 & nbsp空格
                data = data.replace( / % C2 % A0 / g, '%20');
                3 > 再转回来就ok了
                data = decodeURI(data);
                '''
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            # bd = re.sub('<br/(\s+)?/>(\s+)?'," ",bd)
            bd = re.sub('...<br/', " ", bd)
            # bd = re.sub('/'," ",bd)
            bd = re.sub(' '," ",bd)
            data.append(bd.strip())
            datalist.append(data)
    print(datalist)
    return datalist


def askurl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.229 Whale/2.10.123.42 Safari/537.36"
    }
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


def savedata(datelist, savepath):
    print("save...")

    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    col = ('电影详情链接', "图片链接", "影片中文名", "影片外文名", "评分", "评价人数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datelist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)
def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn =sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index ==5:
                continue
            data[index]='"'+data[index]+'"'
        sql ='''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s) '''%" ,".join(data)
        print(sql)
        cur.execute(sql)
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

if __name__ == "__main__":   #加入main函数用于测试程序；
    main()
    print("爬取完毕")