import json
import os
from utils import mysqlconf


def create_book_table():
    try :
        db = mysqlconf.mydb.cursor()
        db.execute("CREATE TABLE books (id INT NOT NULL AUTO_INCREMENT, name varchar(128), author varchar(128),flag INT DEFAULT 0,PRIMARY KEY (id))")
    except:
        pass
    finally:
        db.close()


def get_all_books():
    db = mysqlconf.mydb.cursor()
    _cmd="SELECT * from books"
    db.execute(_cmd)
    books = db.fetchall()
    return books


def add_book(name,author):
    db=mysqlconf.mydb.cursor()
    _cmd = "INSERT INTO books (name,author) VALUES (%s,%s)"
    _data = (name,author)
    db.execute(_cmd, _data)
    db.connection.commit()
    db.close()

# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         json.dump(books, file)


def mark_book_as_read(name):
    name_case=str.capitalize(name)
    print(name_case)
    db=mysqlconf.mydb.cursor()
    _cmd = "UPDATE books SET flag=1 WHERE name=?"
    _data = name_case
    db.execute(_cmd,name_case)
    db.connection.commit()
    db.close()


def delete_book(name):
    name_case = str.capitalize(name)
    db=mysqlconf.mydb.cursor()
    db.execute('DELETE from books WHERE name=?', (name_case,))
    db.connection.commit()
    db.close()
