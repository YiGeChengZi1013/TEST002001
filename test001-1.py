import pymysql
db = pymysql.connect(host='localhost',user='root',password='123qwe',port=3306,db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
sql = 'CREATE TABLE IF NOT EXISTS student (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
db.close()