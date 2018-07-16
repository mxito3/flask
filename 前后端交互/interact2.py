# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-16 10:47:24
# @Last Modified by:   YP
# @Last Modified time: 2018-07-16 11:19:35



#利用flask_cors提供的CORS进行跨域
from flask import Flask,render_template,make_response,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def root():
	return "root"

@app.route('/test')

def test():
	response=make_response(jsonify({'test':'hello world'}))
	return response

if __name__ == "__main__":
	app.run(port=8080,debug=True,host='0.0.0.0')
