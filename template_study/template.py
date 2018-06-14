from flask  import Flask,render_template
from user import User
app=Flask(__name__)

@app.route('/')
def root():
    content="this is content"
    return render_template('index.html',content=content)

@app.route('/userOne/')
def getUser():
    user = User('123456','yapie')
    return render_template('user.html',user=user)
@app.route('/query_user/<userId>')
def query(userId):
    user=None
    if int(userId)==1:
        user=User(1,'yapie')
    return render_template('queryUser.html',user=user)

@app.route('/users')
def getUsers():
    users=[]
    for i in range(1,11):
        users.append(User(i,'yapie'+str(i)))
    return render_template('user.html',users=users)

@app.route('/one')
def one():
    return render_template('one.html')

@app.route('/two')
def two():
    return render_template('two.html')
if __name__=='__main__':
    app.run(debug=True)

