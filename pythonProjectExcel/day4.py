# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/8 13:40
# file:day4.py

import pandas as pd

#平均值，求和；
# students =pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day4\Students.xlsx',index_col='ID')
# temp = students[['Test_1','Test_2','Test_3']]
# row_sum = students[['Test_1', 'Test_2', 'Test_3']].sum(axis=1) #和
# row_mean = students[['Test_1', 'Test_2', 'Test_3']].mean(axis=1) #平均值
# students['Total'] = row_sum #把求和并到表格里
# students['Average'] = row_mean
# col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
# col_mean['Name'] = 'Summary'
# students = students.append(col_mean, ignore_index=True)
# print(students)

# 去掉重复数据；
students = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day4-1\Students_Duplicates.xlsx')
# students.drop_duplicates(subset='Name', inplace=True, keep='first')
# #去除重复的数据；如果不加 keep=' '，只是去除数据；加 keep='first'，去掉后面重复的； keep='last',去掉前面重复的；
# print(students)
# dupe = students.duplicated(subset='Name')
# # print(dupe) #重复的数据，筛选是否有重复数据，如果输出有TRUE，表示有重复数据；
# dupe = dupe[dupe == True]  # dupe = dupe[dupe],便捷的写法，因为dupe就是确定是否有重复的数据，输出为TRUE；
# # print(dupe) #输出重复的数据；
# # print(dupe.index) #索引重复的的列；
# print(students.iloc[dupe.index]) #定位索引到的重复列；

# 表格旋转；
# videos= pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day4-2\Videos.xlsx')
# pd.options.display.max_columns = 999 #为了让表格完全显示；
# table = videos.transpose() #表格旋转；
# print(table)

# 读取csv,txt,tsv文件
# students1 = pd.read_csv('G:\python自动化办公\pandas玩转excel\源代码\day4-3\Students.csv',index_col='ID')
# # print(students1)
# students2 = pd.read_csv('G:\python自动化办公\pandas玩转excel\源代码\day4-3\Students.tsv', sep='\t', index_col='ID')
# print(students2)
# students3 = pd.read_csv('G:\python自动化办公\pandas玩转excel\源代码\day4-3\Students.txt', sep='|', index_col='ID')
# print(students3)

# 分类和汇总；透视表，分组，聚合；
from datetime import date
import numpy as np

pd.options.display.max_columns=999
orders = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day4-4\Orders.xlsx')
orders['Year'] = pd.DatetimeIndex(orders.Date).year
# print(orders.head())
# print(orders.Date.dtype())

# 透视表，，第一种方式；
pt = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)
# print(pt)

#透视表，第二种方式；
# groups = orders.groupby(['Category', 'Year'])
# s = groups['Total'].sum()
# c = groups['ID'].count()
# pt1 = pd.DataFrame({'Sum': s, 'Count': c})
# print(pt1)


