# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/6 20:18
# file:day1.py

'''
#pandas与excel
# import pandas as pd
# df = pd.DataFrame({"ID":[1,2,3],"name":["tim","jack","nina"]}) #函数(),字典类型；
# df = df.set_index('ID') #或people.set.index('id',inplace=True)把ID变成索引一列，就是第一列；没有这行代码的话，id是第二列；
# df = pd.read_excel('E:/pythonProjectExcel/People.xlsx',index_col='id') 加上index_col='id'，表格生成时，id会自动索引为第一列；
# df.to_excel('E:/pythonProjectExcel/day1.xlsx')
# print("done")

# import pandas as pd
# people = pd.read_excel('E:/pythonProjectExcel/People.xlsx')
# print(people.shape) #表格总共多少行，列；
# print(people.columns) #表格的第一行；
# 有时第一行是错误的；加上people = pd.read_excel('E:/pythonProjectExcel/People.xlsx'，header=1；然后再print(people.columns))
# print(people.head(3)) #表很大；所以可以选择看；比如头三行；
# print(people.tail(3)) #表格后三行；

# people=pd.read_excel('E:/pythonProjectExcel/People.xlsx',header=None) #表格没有第一行的目录时；
# people.columns=['id','type','title','firstname'] #加表格的目录
'''

import pandas as pd
from datetime import date,timedelta

# dict={'x':100,'y':200,"z":800}
# s1 =pd.Series(dict) #把字典改成了seris了；打印会出错；
# print(s1.data)

#创建一个序列；
# l1 =[100,200,300]
# l2 = ['x','y','z']
# s1 =pd.Series(l1,index=l2)
# print(s1)
# s1 =pd.Series([100,200,300],index=['x','y','z'])
# print(s1)

'''
s1 =pd.Series([1,2,3],index=[1,2,3],name='A')
s2 =pd.Series([10,20,30],index=[1,2,3],name='B')
s3 =pd.Series([100,200,300],index=[1,2,3],name='C')
df =pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)
'''
# books =pd.read_excel('E:/pythonProjectExcel/Books2.xlsx')
# print(books)
# books= pd.read_excel('E:/pythonProjectExcel/Books2.xlsx',skiprows=3,usecols='C:F',index_col=None,
#                      dtype={'ID':str,'InStore':str,'Date':str})
# # print(books) #把空行去掉，打印正确的表格；
# books['ID'].at[0]=100
# print(books['ID'])

'''
#python中没有月份的时间序列，所以下面定义了月份的函数算法；不然会有13月，14月等；
def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
        return date(d.year + yd, m, d.day) #我运行出错了；日期没有设置成功；

books = pd.read_excel('E:/pythonProjectExcel/Books2.xlsx', skiprows=3, usecols='C:F', index_col=None,
            dtype={'ID': str, 'InStore': str, 'Date': str})
start =date(2018,1,1)
for i in books.index:
    books['ID'].at[i]=i+1
    books['InStore'].at[i]='Yes' if i %2 ==0 else 'No'
    books['Date'].at[i] = add_month(start,i)     # books['Date'].at[i]=start + timedelta(days =i)
books.to_excel('E:/pythonProjectExcel/Books3.xlsx') #保存设置好的表格；表格日期一列出错了；
'''

# 填充表格
books = pd.read_excel('E:/pythonProjectExcel/Books.xlsx',index_col='ID')
# books['Price']=books['ListPrice']*books['Discount'] # 一列乘以一列；也可以一列乘以一个数字，求值；
# for i in books.index: #类似excel运算，单元格对单元格，pandas一般不这么用；但适应于对其中几行几列的单元格操作；
#     books['Price'].at[i]=books['ListPrice'].at[i]*books['Discount'].at[i]
# for i in range(5,19): #迭代循环，其中几行几列的计算；
#     books['Price'].at[i]=books['ListPrice'].at[i]*books['Discount'].at[i]
# books['ListPrice']=books['ListPrice']+2 #直接给这一列进行运算
'''
# def add_2(x):
#     return x +2
# books['ListPrice']=books['ListPrice'].apply(add_2)
books['ListPrice']=books['ListPrice'].apply(lambda x:x+2) #上面三行代码，这一行就可以实现；不用再def函数；
print(books)
'''