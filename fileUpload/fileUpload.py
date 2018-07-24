# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-23 23:45:59
# @Last Modified by:   YP
# @Last Modified time: 2018-07-24 11:06:41
from flask import Flask,request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
uploadFloader='../'
app.config['UPLOAD_FLODER']=uploadFloader
@app.route('/')
def index():
	return "Hello World"
@app.route('/file_upload',methods=['Post'])
def file_upload():
	file=request.files['test']
	file.save(os.path.join(app.config['UPLOAD_FLODER'],secure_filename(file.filename)))
	return "upload success"


if __name__=='__main__':
	app.run(port=8080,debug=True)