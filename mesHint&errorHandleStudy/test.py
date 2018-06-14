from flask import Flask,render_template,flash,request,abort

app=Flask(__name__)
app.secret_key="123456"   #用来加密消息
@app.route('/')
def root():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    form=request.form
    user_name=form.get('user_name')
    user_password=form.get('user_password')
    print(str(user_name)+str(user_password))
    if not user_name:
        flash("请输入用户名")
        return render_template('login.html')
    if not user_password:
        flash("请输入密码")
        return render_template('login.html')
    if str(user_name) == 'yapie' and str(user_password) == "123456":
        flash("login success")
        return render_template('index.html')
    else:
        flash("用户名或密码错误")
        return render_template('login.html')

@app.errorhandler(404)
def catchError(e):
    return render_template('404.html')

@app.route('/user/<userId>')
def getUserId(userId):
    if int(userId)== 1:
        return "your id is 1"
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)