# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/3 23:48
# file:testCloud.py

#课程：学习word_cloud应用的操作；

import jieba #分词：一个句子变成很多词
from matplotlib import pyplot as plt #绘图，数据可视化
from wordcloud import WordCloud #词云
from PIL import Image #图片处理
import numpy as np #矩阵运算
import sqlite3 #数据库

conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql ='select instroduction from movie250'
data = cur.execute(sql)
text =" "
for item in data:
    text = text + item[0]
    # print(item[0]) #把text = text + item[0]注释掉， 运行print(item[0])，可以测试，数据库的连接，看到每部电影的影评；
# print(text)  #不注释，显示所有的影评；分了看cut=jieba.cut(text),注释掉了；
cur.close()
conn.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(string)
print(len(string)) #一共分了多少个词；

img = Image.open(r'.\static\assets\img\tree.jpg') #打开遮罩图片，找到当前py的路径，直接复制路径，
img_array =np.array(img) #将图片转换为数组；
wc = WordCloud(
    background_color="white",
    mask = img_array,
    font_path="STCAIYUN.TTF" #字体所在位置：c:\windows\fonts 字体如果不在c盘，不是中文字体，图片就出错；
)
wc.generate_from_text(string)

#绘制图片；
fig =plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴
# plt.show() #显示生成的词云图片，可以测试，看看图片怎么样；
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500) #dpi=500是清晰度，可以不设立；