import csv
import json
user_input=input(f'Please choose one of the option'
                 f'\n "a" for adding the book\n'
                 f' "d" for adding the book\n '
                 f' "r" for reading the book\n '
                 f' "l" for adding the book\n '
                 f'"q" for quiting the program\n'
                 f' Please enter your option: ')
book_list=[]

def add_book():
    book={
        "name":input(f'please enter book name:'),
        "author":input(f'please enter author name'),
        "flag":True
        
    }
    book_list.append(book)
    with open('output.json','w') as f:
        json.dump(book_list, f)

def read_book():
    with open('output.json','r') as f:
        file_content=json.load(f)
        for value in file_content:
            book=value["name"]
            author=value["author"]
            flag=value["flag"]
            print(book,author,flag)

def list_book():
    with open('output.json','r') as f:
        file_content=json.load(f)
        for value in file_content:
            book=value["name"]
            author=value["author"]
            flag=value["flag"]
            print(book,author,flag)



def delete_book():
    pass

user_conf={
    'a':add_book,
    'd':delete_book,
    'r': read_book,
    'l': list_book
}

def book_app(num):
    num=user_input
    while num != 'q':
          if num in user_conf:
              num=user_conf[num]
              num()
          else:
              print("No Valid input")

          num=input(f'please enter your option:')

book_app(user_input)
print('Thanks for choosing book storage Applications')

        
