# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-23 23:45:59
# @Last Modified by:   YP
# @Last Modified time: 2018-07-24 00:02:45
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"
@app.route('/file_upload',methods=['Post'])
def file_upload():
	file=request.files['test']
	file.save('./test2')
	return "upload success"


if __name__=='__main__':
	app.run(port=8080,debug=True)