"""
author: Roshan Kumar singh
Concerned with storing the retreving books from a csv file.
Format of data in file

Name,author,read\n
"""
import json

books_file='books.json'

def create_books_file():
    with open(books_file,'w') as file:
        pass

def add_book(name,author):
    with open(books_file,'a') as f:
        f.write(f'{name},{author},0\n')


def get_all_book():
    with open(books_file, 'r') as f:
        lines=[line.strip().split(',') for line in f.readlines()]
        return[
            {'name':line[0],'author':line[1],'read':line[2]}
             for line in lines
             ]
# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         for book in books:
#             file.write(f"{book['name']},{book['author']},{book['read']}\n")
#
#
# def mark_book_as_read(name):
#     books = get_all_book()
#     for book in books:
#         if book['name'] == name:
#             book['read'] = '1'
#     _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
              file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name):
    books = get_all_book()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)



# Bad practice for removing elements from list
# def delete_book(name):
#     for book in books:
#         if books['name']=name:
#             books.remove(book)


def delete_book(name):
    books=get_all_book()
    books=[book for book in books if book['name'] != name]
    _save_all_books(books)


