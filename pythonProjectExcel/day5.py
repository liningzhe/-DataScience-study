# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/8 16:07
# file:day5.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# # 数据预测；线性回归；
# sales = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day5\Sales.xlsx', dtype={'Month': str, 'Revenue': float})
#
# slope, intercept, r_value, p_value, std_err = linregress(sales.index, sales.Revenue)
# exp = sales.index * slope + intercept
#
# plt.scatter(sales.index, sales.Revenue)
# plt.plot(sales.index, exp, color='red')
# plt.title(f'y={slope}*x+{intercept}')
# plt.xticks(sales.index, sales.Month, rotation=90)
# plt.tight_layout()
# plt.show() #构造回归方程；
# print(slope*35+intercept) #比如计算2019年的预测值；即35个月后；


#关于自动备注最高分最低分，设置背景色等，做了三个表在jupyter notebook；

# 行操作：
# page_001 = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day5-2\Students.xlsx', sheet_name='Page_001')
# page_002 = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day5-2\Students.xlsx', sheet_name='Page_002')

# 追加已有
# students = page_001.append(page_002).reset_index(drop=True)

# 追加新建
# 第一种；追加一行数据；
# stu = pd.Series({'ID': 41, 'Name': 'Abel', 'Score': 99})
# students = students.append(stu, ignore_index=True)
# # 第二种；修改这行数据；
# stu = pd.Series({'ID': 40, 'Name': 'jack', 'Score': 120})
# students.iloc[39]= stu

# 删除（可切片）
# students.drop(index=students[33:37].index,inplace =True)
#
# # 插入，利用切片；
# stu = pd.Series({'ID': 100, 'Name': 'Bailey', 'Score': 100})
# part1 = students[:21]  # .iloc[] is the same
# part2 = students[21:]
# students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)
# print(students)

# 设置空值
# for i in range(5,10):
#     students['Name'].at[i]=''  #把这行数据设为空；
# # 去掉空值
# missing = students.loc[students['Name']=='']
# students.drop(index=missing.index,inplace=True)  #把空的数据移出去；
# students= students.reset_index(drop=True)  #重铺一下表？？
# print(students)

# 列操作
page_001 = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day5-3\Students.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('G:\python自动化办公\pandas玩转excel\源代码\day5-3\Students.xlsx', sheet_name='Page_002')

students = pd.concat([page_001,page_002]).reset_index(drop=True) #连接两个表；串联两个表；
# students = pd.concat([page_001,page_002],axis=1) #并联两个表；

# # 追加列, 可以有不同的函数，灵活使用；
# students['Age'] = 25
# students['Age'] = np.repeat(25,len(students))
# students['Age'] = np.arange(0,len(students))

# # 删除列
# students.drop(columns=['Score', 'Age'], inplace=True)
#
# # 插入列
# students.insert(1, column='Foo', value=np.repeat('foo', len(students)))

# # 改列名
# students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)

# # 设置空值
# students['ID'] = students['ID'].astype(float)  #设置空值，先改成浮点数类型；
# for i in range(5, 15):
#     students['ID'].at[i] = np.nan
#
# # 去掉空值
# students.dropna(inplace=True)

# print(students)