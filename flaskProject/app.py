from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应的函数；

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello,nini!'
#debug模式on的开启模式下，有助于看到错误；

@app.route('/index')
def hello():
    return "hello"

# 通过访问路径，获取用户的字符串参数
@app.route('/user/<name>')
def welcome(name):
    return "hello,%s"%name

#通过访问路径，获取用户的整型参数；此外，还有float类型<float：什么什么>
@app.route("/user/<int:id>")
def welcome2(id):
    return "hello,%d号的会员"%id

#路由路径不能重复，用户通过唯一路径访问特定的函数；比如上面写的user/<name>,user/<int:id>,就是不同的

#返回给用户渲染后的网页文件；
# @app.route("/")
# def index2():
#     return render_template("index.html")

#向页面传递一个变量；
@app.route("/")
def index2():
    time =datetime.date.today() #普通变量；
    name =['jack','rose','nini'] #list类型；
    task ={'任务':'打扫卫生','时间':'3小时'} #字典类型；
    return render_template("index.html",var = time,list= name,task =task)

#表单提交
@app.route('/test/register')
def register():
    return render_template('test/register.html')

#接收表单提交的路由，需要指定methods为post请求，如果只为get请求，会报错405；
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result =request.form
        return render_template('test/result.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
