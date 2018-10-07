import pymysql
class Sql:
    def __init__(self,host,port,user,passwd,db):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
    def connect(self):
        self.con=pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)
        self.cursor=self.con.cursor()
    def close(self):
        self.con.close()
    def extractSql(self,command):
        self.cursor.execute(command)
        self.con.commit()
        return self.cursor.fetchall()