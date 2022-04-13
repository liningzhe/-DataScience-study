# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 16:25
# file:Day2.py
# 文件操作，异常处理；
'''
f = open("test.txt","w") #文件打开模式；后面加w，是写模式：如果没有文件，就会创建文件；
f.close() #关闭打开的文件
'''

'''
f = open("test.txt","r") #r是只读模式： open();open(文件名，什么类型的模式）
f.close()
f = open("test.txt","r")
content = f.read(5) #读取指定的字符，开始时定位在字符串头部；f.read()
print(content)
f.close()
f = open("test.txt","r")
content = f.readlines() #一次性读取全部文件为列表，每行一个字符串元素; f.readlines(),读文件的所有行；
print(content)
f.close()
'''

'''
# 这块代码，自己写的，虽然运行OK，可能有问题；
f = open("test.txt","r")
content = f.readlines() #一次性读取全部文件为列表，每行一个字符串元素; f.readlines(),读文件的所有行；
i =1
for temp in content:
    print("%d:%s"%(i,temp))
    i +=1
content = f.readline()  #读相应行 f.readline()
f.close()
'''

#捕获异常，这块需要重新学习；
'''
import time
try:
    f = open('test.txt','r')
    try:
        while True:
            content =f.readline()
            if len(content) ==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print('文件关闭')
except Exception as result:
    print("发生异常")
'''
# try:
#     print("test1")
#     f = open("函数.py","r")#只读模式打开了一个不存在的文件会报错
#     print("test2")#报错后 后面的不会再运行
#     print(num) #没有命名变量，错误
# except (NameError,IOError) as result:  #文件没有找到（输入输出异常)；将可能出现的错误，都放到下面的小括号中
#     pass  #捕获异常后，执行
# except (Exception) as result: #exception可以承接任何异常
#     print(result)
# try ----finally 和嵌套
# try:
#     f = open('123.txt','r')
# except Exception as result:
#     print("发生异常")
# finally:
#     f.close()
#     print('文件关闭')