from flask import  Flask,render_template,request,flash,redirect
import pymysql
app=Flask(__name__)
app.secret_key='123456'
@app.route('/')
def root():
    return render_template('signIn.html')

@app.route('/login',methods=['Post'])
def login():
    form = request.form
    user_name = form.get('user_name')
    user_passwrd = form.get('user_password')
    #判断是否存在该用户名和密码
    result=extractSql('login',(user_name))
    print(result)
    print("密码")
    #print(result[0][0])
    print("密码")
    print(user_passwrd)
    if len(result)!=0 and str(result[0][0])==user_passwrd:
        return redirect("https://github.com/mxito3")
    else:
        flash("用户名和密码不匹配")
        return render_template('login.html')



@app.route('/signIn',methods=['Post'])
def signIn():
    form=request.form
    user_name=form.get('user_name')
    user_password=form.get('user_password')
    print(user_name)
    print(user_password)
    extractSql('insert',(user_name,user_password)) #存入数据库
    checkwhetherFinish='select user_password from user where user_name=user_name'
    if len(extractSql('',checkwhetherFinish))!=0:
        flash("注册成功")
        return render_template('login.html')
    else:
        flash("注册失败")
        return render_template('signIn.html')

def extractSql(commadType,arguments):
    print("参数"+str(arguments))
    con=pymysql.connect("120.27.11.67","root","domore0325","blog")
    cursor=con.cursor()
    if commadType=='insert':
        cursor.execute('insert into user(user_name,user_password) values (%s,%s)',(arguments[0],arguments[1]))
        con.commit()
    elif commadType=='login':
        cursor.execute("select user_password from user where user_name=%s",arguments)
    else:
        cursor.execute(arguments)
    data=cursor.fetchall()
    return  data
if __name__ ==  '__main__':
    app.run(debug=True)