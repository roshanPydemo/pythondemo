import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="12345",
  database="demodb"
)

cursor = mydb.cursor()
cursor.execute("CREATE TABLE books (id varchar(128), name varchar(128), author varchar(128),flag int DEFAULT 0,PRIMARY KEY (`id`))")
cursor.close()