# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/5 14:55
# file:基础练习.py
'''
# 商品项目
products = [['iphone',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',64],['NIKE',699]]
print('------商品列表------')
# for i in range(len(products)):
#     print(i,"%s"%products[i][0]+"\t"+"%d"%products[i][1]+"\t") #i决定项目的排序，老方法；
for i, x in enumerate(products):
    print(i,x)
'''

"""
这块我自己的理解；
# 第一步，定义函数；#只是定义一个函数，程序不会自动执行函数，需要调用这个函数；
def sum(a,b):
#第二步，调用函数；调用函数，并保存函数的返回值；
    return a+b
#第三步，因为第二步return已经保存了函数的返回值，接下来就可以使用；
sum(100,200)
print(sum(100,200))
"""
# import os
# os.rename("基础练习.py","基础学习.py") #重命名；前：原来名字；后：新名字；改为会关闭窗口；

# 爬虫主流程一：
from urllib import parse
kw = input("请输入你要搜索的岗位关键字：")
keyword = parse.quote(parse.quote(kw))
pageNum =1
def main():
    # initDB()初始化？什么意思；
    url ="https://search.51job.com/list/360000,000000,0000,00,9,99,"+keyword+",2,"+str(pageNum)+".html"
    # %25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE = 输入的关键字，（ "+keyword+" ）；
    # 提前引入parse模板，进行转义，这样用户输入；
    # html =askurl(url)
    print(url) #网址的解析
