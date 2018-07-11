
from flask import Flask,render_template,url_for,request,flash
import pymysql
import sys
sys.path.append(r'D:\github\flask\blog')
from config import sql
app=Flask(__name__)
app.secret_key=123456
sq=sql.Sql("localhost",3306,'root','domore0325','blog')
@app.route('/')
def root():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/login',methods=['Post'])
def login():
    form=request.form
    userName=form.get('userName')
    password=form.get('password')
    #查询
    sq.connect()
    command='select password from user where userName='+"'"+str(userName)+"'"
    print(command)
    data=sq.extractSql(command)
    sq.close()
    print('数据是')
    print(data)
    articles=None
    if data and data[0][0]==password:
        #flash("login sucess")
        return render_template('index.html',articles=articles)
    else:
        flash("用户名密码不匹配")
        return render_template('login.html')

@app.route('/addComment',methods=['Post'])
def addComment():
    form=request.form
    title=form.get('title')
    comment=form.get('comment')
    #写进数据库
    command='insert into blog(title,comment)values '+'('+"'"+title+"','"+comment+ "')"
    print("命令是"+command)
    sq.connect()
    sq.extractSql(command)
    data = list(sq.extractSql('select title,comment from blog'))[::-1]
    sq.close()
    return render_template('index.html',articles=data)

if __name__=="__main__":
    app.run(debug='true',port=8080)

