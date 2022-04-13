# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/2 17:06
# file:Day3.py
# 练习题1：小游戏和随机分配办公室
# 条件判断
import random
player = int(input("输入: knife(0),stone(1),paper(2):"))
computer = random.randint(0,2)
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 0):
    print("我赢了!")
elif player == computer:
    print("平局")
else:
    print("不玩了！！")
# 讲课视频中 有游戏版操作，这是正常版，可以有不同的思维，等代码熟悉之后
# 随机分配办公室
import random
offices= [[],[],[]]
schoolteacher=["小可爱","rose","然然","宁哲","李阁","jhon","jack","lucy"]
for name in schoolteacher:
    index = random.randint(0,2)
    offices[index].append(name)
i=1
for office in offices:
    print("办法室%d的人数为：%d"%(i,len(office)))
    i +=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
# 练习题2：购买商品的项目
# print("商品列表"); {Python里不建议用分号，所以会报错；但对运行没有太大关系；但是其他语言，有的需要分号，所以看情况；
products = [["iphone",6888],["macpro",14800],["redmi",2499],["coffee",30],["book",50],["nike",699]]
i = 0
for item in products:
    print(str(i)+ "\t" +item[0]+"\t"+str(item[1]))
    i +=1 #第一种
for i,item in enumerate(products): #这里可使用enumerate函数，即列举函数，因为前面排序有0,1,2,3-----
    print( str(i)+"\t"+item[0]+"\t"+str(item[1])) #第二种
# 根据上面的产品列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购物列表