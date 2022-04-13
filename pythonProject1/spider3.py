# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 17:51
# file:spider3.py

#保存数据到xlmt
import xlwt
# workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象；
# worksheet = workbook.add_sheet('sheet1') #创建工作表；
# worksheet.write(0,0,'hello') #写入数据，第一行参数是行，第二个参数是列，第三个参数是内容；

#打印九九乘法表；
workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象；
worksheet = workbook.add_sheet('sheet1') #创建工作表；

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d*%d=%d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')  #保存数据表；
