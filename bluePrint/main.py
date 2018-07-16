# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-16 18:23:45
# @Last Modified by:   YP
# @Last Modified time: 2018-07-16 19:12:13
from flask import Flask 
from test import test
from user import user
app = Flask(__name__)
app.register_blueprint(user.mod)  #参数是Blueprint实例
app.register_blueprint(test.mod)
@app.route('/')
def root():
	return "this is root"
if __name__=='__main__':
	app.run(port=8080,debug=True,host='0.0.0.0')