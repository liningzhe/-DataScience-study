# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 15:56
# file:Day1.py

'''
#打印几行的横线
def a():
    print("-"*5)
def b(num):
    i=0
    while i<num:
        a()
        i +=1
b(5)
'''

'''
#求三个数的和与平均值；
def add3num(a,b,c):
    return(a+b+c)
add3num(2,3,4)
print(add3num(2,3,4))
def averge3num(a,b,c):
    sum = add3num(10,20,30)
    ave =sum/3.0
    return ave
result = averge3num(10,20,30)
print("ave:%d"%result)  
'''

'''
#全局变量和局部变量
a = 100
def test1():
    global a
    print(a)
    a =200
    print(a)
def test2():
    print(a)
    print(a)
test1()
test2()
'''

'''
#日期和时间
import time
ticks = time.time()
print("now time:",ticks) # = 时间戳，即1970年到此刻多少秒：
localtime = time.asctime(time.localtime(time.time()))
print("当地时间：",localtime) #获取格式化的日期
'''

'''
#选代器和生成器  #这块有待再看看，没有太大意义，下面写的；
list = [1,2,3,4]
it = iter(list)
print(next(it))
print(next(it))
python = iter("python")
print(python)
for i in python:
    print(i)
'''

# return 语句
def sum(a,b):
    total = a+b
    print("函数内：",total)
    return total #返回两个函数的和
total = sum(10,20) #调用sum函数
print("函数外: ",total)

