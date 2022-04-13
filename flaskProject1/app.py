from flask import Flask,render_template
import sqlite3

app = Flask(__name__) #初始化


@app.route('/')
def index():  # put application's code here
    return render_template('index.html') #这样相当于打开网页； #这里注意路径问题

@app.route('/index')
def home():
    # return render_template('index.html') #这样点首页，会不出错；相当于建立首页的链接；
    return index()  #两种方式都可以；

@app.route('/movie')
def movie():
    datalist = []
    conn =sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('movie.html',movies = datalist)


@app.route('/score')
def score():
    score = [] #评分
    num = [] #相同评分的电影数量；
    conn =sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select score,count(score) from movie250 group by score'
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0])) #score.append(item[0])，如果网页源码是字符串类型，要进行转换；不然网页运行会出错；
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template('score.html',score=score,num=num)

@app.route('/word')
def word():
    return render_template('word.html')

@app.route("/team")
def team():
    return render_template('team.html')






if __name__ == '__main__':
    app.run()
