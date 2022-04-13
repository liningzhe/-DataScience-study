# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/13 22:07
# file:day6.py

# import pyodbc      #连接数据库
# import sqlalchemy
# import pandas as pd
#
# connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=(local); DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')
# query = 'SELECT FirstName, LastName FROM Person.Person'
# engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks?driver=SQL+Server')
#
# df1 = pd.read_sql_query(query, connection)
# df2 = pd.read_sql_query(query, engine)
#
# pd.options.display.max_columns = 999
# print(df1.head())
# print(df2.head())

# 计算复杂函数
import pandas as pd
import numpy as np

def get_circumcircle_area(l, h): #定义外接圆面积的函数
    r = np.sqrt(l ** 2 + h ** 2) / 2
    return r ** 2 * np.pi

# def wrapper(row): #不想定义这个函数，可以用lambda函数，第二种方式更便利；
#     return get_circumcircle_area(row['Length'], row['Height'])
#
# rects = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day6-1\Rectangles.xlsx', index_col='ID')
# rects['CA']=rects.apply(wrapper,axis=1) #如何扫描表；

rects = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day6-1\Rectangles.xlsx', index_col='ID')
rects['CA']=rects.apply(lambda row: get_circumcircle_area(row['Length'], row['Height']),axis=1) #如何扫描表；

print(rects)