import pymysql

id = '20181031'

user = 'Bob'
age = 20
db = pymysql.connect(host='localhost',user='root',password='123qwe',port=3306,db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO student(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commint()
except:
    db.rollback()
db.close()