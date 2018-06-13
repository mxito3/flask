
from flask import Flask,request,url_for
app = Flask(__name__)

@app.route('/')
def root():
    return 'root'

@app.route('/hello/')
def hello():
    return 'hello'

#从url获取属性
@app.route('/user/<id>')
def getUser(id):
    return 'hello'+id
#从request获取属性，访问root_url/users?id="123456"
@app.route('/users/')
def getIdByRequest():
    return 'your id is '+ request.args.get('id')

#反向路由
@app.route('/getUrl/<functionName>')
def getUrl(functionName):
    return url_for(functionName)

if __name__ == '__main__':
    app.run(debug=True)
