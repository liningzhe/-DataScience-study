# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/7 1:24
# file:day3.py

import pandas as pd
import matplotlib.pyplot as plt

'''
homes = pd.read_excel('G:/python自动化办公/pandas玩转excel/源代码/day3/home_data.xlsx')
# 散点图
# pd.options.display.max_columns = 999  #把输出结果的隐藏部分的列 显示出来
# print(homes.head())   #表格太长，只输出head；
# homes.plot.scatter(x='sqft_living', y='price') #把x，y的位置换一下，坐标轴位置就换了；
# plt.show()
# 直方图
# homes.price.plot.hist(bins=200) #bins值为了让直方图显示更合理；
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
# plt.xticks(range(0, max(homes.price), 100000), fontsize=8, rotation=90)
# plt.show()
# 密度图
# homes.sqft_living.plot.kde()
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
# plt.show()

# x,y轴的相关性；
# pd.options.display.max_columns = 999  #把输出结果的隐藏部分的列 显示出来
# print(homes.corr()) #corr()

# 一个excel文件里面的两个表格横向，连接；excel里使用vlookup函数；
# students = pd.read_excel('E:/pythonProjectExcel/Student_score.xlsx', sheet_name='Students')
# scores = pd.read_excel('E:/pythonProjectExcel/Student_score.xlsx', sheet_name='Scores')
# table = students.merge(scores, how='left', on='ID').fillna(0) #finallna(0)函数，null变成0：
# table.Score = table.Score.astype(int)  #浮点数变成整型数；
# print(table)

# students = pd.read_excel('E:/pythonProjectExcel/Student_score.xlsx', sheet_name='Students', index_col='ID')
# scores = pd.read_excel('E:/pythonProjectExcel/Student_score.xlsx', sheet_name='Scores', index_col='ID')
# table = students.merge(scores, how='left', left_on=students.index, right_on=scores.index).fillna(0)
# table.Score = table.Score.astype(int) #如果id设为index，那么id就不再是普通列；所以要重新指定index 索引；
# print(table)

# students = pd.read_excel('E:/pythonProjectExcel/Student_score.xlsx', sheet_name='Students', index_col='ID')
# scores = pd.read_excel('E:/pythonProjectExcel/Student_score.xlsx', sheet_name='Scores', index_col='ID')
# table = students.join(scores, how='left').fillna(0)
# table.Score = table.Score.astype(int)  #.join()函数；
# print(table)
'''
# 数据校验
# students =pd.read_excel("G:\python自动化办公\pandas玩转excel\源代码\day3-2\Students.xlsx")
# # 数字校验：数据是否错误；在做校验时，尽量不要设置index，这样的话，所有的列都是普通列，方便数据校验；
# # def score_validation(row):
# #     try:
# #         assert 0<=row.Score<=100
# #     except:
# #         print(f'#{row.ID}\tstudent {row.Name} has an invaild score.{row.Score}') #加\t,制表符；对齐；
#     #或者用
# def score_validation(row):
#     if not 0 <= row.Score<=100:
#         print(f'#{row.ID}\tstudent {row.Name} has an invaild score.{row.Score}')
# students.apply(score_validation,axis=1)

# # 一列数据分列成两列；
# employees = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day3_3\Employees.xlsx',index_col='ID')
# df = employees['Full Name'].str.split(n=2,expand =True) #这里的n，可以加或者不加，不加就全部显示；
# employees['First Name'] = df[0].str.upper() #.str.upper() 变成大写：
# employees['Last Name'] = df[1]
# print(employees)