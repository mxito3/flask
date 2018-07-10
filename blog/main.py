from flask import Flask,render_template,url_for,request,flash
import pymysql

app=Flask(__name__)
app.secret_key=123456
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
    con=pymysql.connect(host="localhost",user='root',passwd='domore0325',db='blog',port=3306)
    cursor=con.cursor()
    cursor.execute('select password from user where userName=%s',userName)
    data=cursor.fetchone()
    con.close()
    print(data)
    articles=None
    if not data is None and data[0] == password:
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
    con=pymysql.connect(host='localhost',user='root',passwd='domore0325',db='blog',port=3306)
    cursor=con.cursor()
    cursor.execute('insert into blog(title,comment)values (%s,%s)',(title,comment))
    con.commit()
    cursor.execute('select title,comment from blog')
    data = list(cursor.fetchall())[::-1]
    con.close()
    return render_template('index.html',articles=data)

if __name__=="__main__":
    app.run(debug='true',port=8080)
