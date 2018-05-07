#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import pymysql
#打开数据库连接
db=pymysql.connect("localhost","root","","mysql")

#使用cursor()创建一个游标对象
cursor=db.cursor()

#使用execute()方法查询数据库
cursor.execute("select version()")

#使用fetchone取回单条数据
data=cursor.fetchone()

print("database version: %s"%data)

#关闭数据库
db.close()


