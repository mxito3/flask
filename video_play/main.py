import os
from pathlib import Path
import uuid
from flask import Flask,render_template,url_for,request,redirect,flash,request,session
from werkzeug.utils import secure_filename
from config.sql import Sql
app=Flask(__name__)
app.secret_key=bytes(str(uuid.uuid4()),'utf-8')
sql=Sql("localhost",3306,'root','domore0325','videos')
uploadFloader='./static/upload'
app.config['UPLOAD_FLODER']=uploadFloader

@app.route('/play')
def root():
    #return url_for('static',filename='js/index.css')
    videos=checkExists()
    return render_template('index.html',videos=videos)

@app.route('/admin')
def admin():
    return render_template('admin.html')
# insert into videoMap (id,title)values("4d2121d2-8d9c-407e-9a77-75e948774a18","小姐姐唱歌的小视频");

@app.route('/upload',methods=['Post','GET'])
def file_upload():
    if request.method == 'POST':
        if 'admin' in session['username']:
            file=request.files['test']
            title=request.form.get('title')
            print(title)
            rawFileName=file.filename
            if title=="" or rawFileName=="":
                mes="未填标题或未选择文件,请重新上传"
            else:
                fileId=str(uuid.uuid4())
                fileName=fileId+".mp4"
                file.save(os.path.join(app.config['UPLOAD_FLODER'],fileName))
                sql.connect()
                command='insert into videoMap(id,title)values('"'%s'"','"'%s'"')'%(fileId,title)
                print(command)
                sql.extractSql(command)
                sql.close()
                mes="upload file '"+rawFileName +"' with success"
            return mes
        else:
            flash('请先登录')
            return redirect('/login')
    else:
        flash('请先登录')
        return redirect('/login')


@app.route('/',methods=['GET'])
def videoList():
    videos=checkExists();
    return render_template('videoList.html',videos=videos)


@app.route('/login',methods=['Post','GET'])
def signIn():
    if request.method == 'POST':
        form=request.form
        user_name=form.get('user_name')
        user_password=form.get('user_password')
        session['username']=user_name
        print(user_name)
        print(user_password)
        if user_name == 'admin' and user_password =='domore0325':
            return render_template('/admin.html')
        else:
            flash("用户名密码不匹配")
            return render_template('login.html')
    else:
        return render_template('/login.html')


# 判断数据库存的视屏是否在服务器存在
def checkExists():
    sql.connect()
    command='select * from videoMap'
    result=sql.extractSql(command)
    videos=[]
    videoIndex=1
    for item in result:
        videoItem={}
        videoName=item[0]+".mp4"

        if existSuchViedo(videoName):
            videoItem['path']="/static/upload/"+videoName
            videoItem['title']=item[1]
            videoItem['index']=videoIndex
            videos.append(videoItem)
            videoIndex +=1
    sql.close()
    for item in videos:
        print(item)
        # print(item[1])
    return videos

def existSuchViedo(name):
    myfile=Path(os.path.abspath(uploadFloader)+"/"+name)
    if myfile.is_file():
        return True;
    else:
        return False



if __name__=="__main__":
    app.run(host='0.0.0.0',debug='true',threaded=True,port=8080)
