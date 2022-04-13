# -*- coding: utf-8 -*-
# Author：Nina
# Time:2021/9/6 23:09
# file:day2.py

import matplotlib.pyplot as plt
import pandas as pd

"""
# 排序问题：
products =pd.read_excel('E:/pythonProjectExcel/List.xlsx',index_col="ID")
# products.sort_values(by='Price',inplace=True,ascending=False) #按价格排序；
# products.sort_values(by='Worthy',inplace=True,ascending=False) #按价格排序；
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False]) #同时操作两列的排序；
print(products)
"""

"""
# 筛选：
# students = pd.read_excel('E:/pythonProjectExcel/Students.xlsx',index_col="ID")
# def age_18_to_30(a):
#     return 18 <=a <30
# def level_a(s):
#     return 85 <= s <=100
# students=students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)] #简洁写法；
# # students =students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]
# print(students)

students = pd.read_excel('E:/pythonProjectExcel/Students.xlsx',index_col="ID")
# students=students.loc[students.Age.apply(lambda a:18<=a<30)].loc[students.Score.apply(lambda s:85<=s<=100)] #简洁写法；
students=students.loc[students.Age.apply(lambda a:18<=a<30)]\
    .loc[students.Score.apply(lambda s:85<=s<=100)] #简洁写法； 代码一行过长时，加一个后划线即可下一行；
print(students) #使用lambda，最简单的写法；不用再定义函数；
"""

'''
#柱状图1
import matplotlib.pyplot as plt
students = pd.read_excel('E:/pythonProjectExcel/Students2.xlsx')
students.sort_values(by='Number',inplace=True,ascending=False) #排序数据；
print(students)
students.plot.bar(x='Field',y='Number',color='green',title='International Students by Filed') #图的颜色；x，y轴；
# plt.bar(students.Field,students.Number,color='red') #用plt制作图；
# plt.xticks(students.Field,rotation='90')
# plt.xlabel("Field")
# plt.xlabel('Number')
# plt.title("International Students by Filed",fontsize=16)
plt.tight_layout() #图紧凑一些，标签全部显示；
plt.show() #输出图

# 柱状图2
students = pd.read_excel('E:/pythonProjectExcel/Students3.xlsx')
students.plot.bar(x="Field",y=['2016','2017'],color=['orange','yellow'])
plt.title('International Students by Filed',fontsize=16,fontweight='bold')
plt.xlabel('Field',fontweight='bold')
plt.xlabel('Number',fontweight='bold')
ax = plt.gca()
ax.set_xticklabels(students['Field'],rotation=45,ha='right') #标签斜体；
f = plt.gcf()
f.subplots_adjust(left=0.2,bottom=0.45)
plt.tight_layout() #图紧凑一些，标签全部显示；
plt.show() #输出图

#柱状图3
users = pd.read_excel('E:/pythonProjectExcel/Users.xlsx')
users['Total']=users['Oct']+users['Nov']+users['Dec']
users.sort_values(by="Total",inplace=True)
users.plot.barh(x="Name",y=['Oct','Nov','Dec'],stacked=True,title="User Bahavior") #水平排序；
plt.tight_layout()
plt.show()
'''
'''
# 饼图
students =pd.read_excel('E:/pythonProjectExcel/Students4.xlsx',index_col="From")
students['2017'].plot.pie(fontsize=5,counterclock=False) #把表顺时针，逆时针；
plt.title('source of students',fontsize=16,fontweight='bold')
plt.ylabel('2017',fontsize=12,fontweight='bold')
plt.show()
'''
# 折线图
orders =pd.read_excel('E:/pythonProjectExcel/Orders.xlsx',index_col="Week")
orders.plot.area(y=['Accessories','Bikes','Clothing', 'Components']) #叠加折线图，重合部分叠加；不叠加时，不加area；
plt.title('sales weekly trend',fontsize=16,fontweight='bold')
plt.ylabel("Total",fontsize=12,fontweight='bold')
plt.xticks(orders.index,fontsize=8)
plt.show()