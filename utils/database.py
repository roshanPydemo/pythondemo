

books=[]

def add_book(name,author):
    books.append({'name':name,'author':author,'read':False})

def get_all_book():
    return books

def mark_read_book(name):
    for value in books:
        if name==value['name']:
            value['read']=True

# Bad practice for removing elements from list
# def delete_book(name):
#     for book in books:
#         if books['name']=name:
#             books.remove(book)

def delete_book(name):
    global books
    books = [ book for book in books if book['name'] != name]

