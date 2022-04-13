# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 17:58
# file:spider5.py

#bs4模块的使用；

# BeautifulSoup是python解析html非常好用的第三方库；
# BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,BeautifulSoup4四大对象种类:
#（1）Tag： 通俗点讲就是HTML中的一个个标签
#（2）NavigableString：获取标签内部的文字用 .string即可
#（3）BeautifulSoup：表示的是一个文档的内容
#（4）Comment：是一个特殊类型的 NavigableString对象，其输出的内容不包括注释符号；

from bs4 import BeautifulSoup
file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")
'''
print(bs.title)
print(bs.a)
print(bs.head)
print(type(bs.head))  #tag;标签及其内容；默认
print(bs.title.string)
print(type(bs.title.string))  #NavigableString，标签里的内容；
print(bs.a.attrs) #一个标签里的所有属性；
print(type(bs))
print(bs.name) #表示整个文档；
print(bs.attrs) # 什么类型的标签；
print(bs) #整个文档的内容；
print(bs.a.string)
print(type(bs.a.string)) #是一个特殊类型的 NavigableString对象，其输出的内容不包括注释符号;
'''


# 文档的遍历，遍历文档树
# print(bs.head.contents)
# print(bs.head.contents[1])

# 文档的搜索；搜索遍历，更广泛使用；

# 第一种：find_all() 字符串过滤：会查找与字符串完全匹配的内容；
# t_list= bs.find_all("a")
# print(t_list)

# 第二种：正则表达式搜索：使用search()方法来匹配内容；
# import re
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

# 第三种：方法：传入一个函数（方法），根据函数的要求来搜索；自定义函数；
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)
# print(t_list)

# 第四种 kwargs参数
# t_list = bs.find_all(id="head")
# for item in t_list:
#     print(item)
# t_list =bs.find_all(class_=True)
# for item in t_list:
#     print(item)
# t_list =bs.find_all(href="http://news.baidu.com")
# for item in t_list:
#     print(item)

# 第五种 text文本参数
# t_list =bs.find_all(text="hao123")
# for item in t_list:
#     print(item)
# t_list =bs.find_all(text=["hao123","地图","贴吧"])
# for item in t_list:
#     print(item)
# import re
# t_list = bs.find_all(text= re.compile("\d")) #应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)

# 第六种 limit参数
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)


# css选择器

# t_list = bs.select("title") #通过标签来查找；
# for item in t_list:
#     print(item)
# t_list = bs.select(".mnav") #通过类名来查找；
# for item in t_list:
#     print(item)

print(bs.select('#u1')) #通过id来查找；
print(bs.select('div .bri'))#通过组合来查找；
print(bs.select('a[class="bri"]'))  #通过属性来查找
print(bs.select('a[href="http://tieba.baidu.com"]')) #通过属性来查找
print(bs.select("head> title"))  # 通过子标签来查找；
print(bs.select(".mnav ~ .bri"))  #通过兄弟节点标签来查找；
print(bs.select('title')[0].get_test()) #获取内容；
