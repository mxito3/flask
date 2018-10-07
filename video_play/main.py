import os
from pathlib import Path
import uuid
from flask import Flask,render_template,url_for,request,redirect,flash,request
from werkzeug.utils import secure_filename
from config.sql import Sql
app=Flask(__name__)
app.secret_key=bytes(str(uuid.uuid4()),'utf-8')
sql=Sql("localhost",3306,'root','domore0325','videos')
uploadFloader='./static/upload'
app.config['UPLOAD_FLODER']=uploadFloader
@app.route('/')
def root():
    #return url_for('static',filename='js/index.css')
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
# insert into videoMap (id,title)values("4d2121d2-8d9c-407e-9a77-75e948774a18","小姐姐唱歌的小视频");

@app.route('/upload',methods=['Post'])
def file_upload():
    file=request.files['test']
    title=request.form.get('title')
    print(title)
    rawFileName=file.filename
    fileId=str(uuid.uuid4())
    fileName=fileId+".mp4"
    file.save(os.path.join(app.config['UPLOAD_FLODER'],fileName))
    sql.connect()
    command='insert into videoMap(id,title)values('"'%s'"','"'%s'"')'%(fileId,title)
    print(command)
    sql.extractSql(command)
    sql.close()
    mes="upload file "+rawFileName +" with success"
    return mes
    # return redirect('/admin')
# 判断数据库存的视屏是否在服务器存在
def checkExists():
    sql.connect()
    command='select id from videoMap'
    result=sql.extractSql(command)
    videos=[]
    for item in result:
        videoName=item[0]+".mp4"
        if existSuchViedo(videoName):
            videos.append(videoName)
    sql.close()
    print(videos)

def existSuchViedo(name):
    myfile=Path(os.path.abspath(uploadFloader)+"/"+name)
    if myfile.is_file():
        return True;
    else:
        return False



if __name__=="__main__":
    # app.run(host='0.0.0.0',debug='true',port=8080)
    checkExists()
    

    