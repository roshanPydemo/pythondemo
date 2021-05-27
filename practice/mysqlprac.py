from utils import database4

USER_CHOICE = """
- 'a' to add a book 
- 'l' to list all books
- 'd' to delete a book 
- 'r' to mark read a book
- 'q' to quit 
Your choice:"""

def menu():
    database4.create_book_table()
    user_input= input(USER_CHOICE)
    while user_input!='q':
        if user_input == 'a':
            prompt_add_book()
        elif  user_input == 'l':
            prompt_list_book()
        elif  user_input == 'd':
            prompt_delete_book()
        elif user_input == 'r':
            prompt_read_book()
        else:
            print("unknow command. Please try again")
        user_input=input(USER_CHOICE)

# Prompt add book for adding the book name and author
def prompt_add_book():
    name=input("Enter the book name:")
    author=input("Enter the author name")
    database4.add_book(name,author)

# Prompt add book for listing all the book name and author
def prompt_list_book():
    books=database4.get_all_books()
    for book in books:
        read = 'Yes' if book[3] else 'No'
        print(f' {book[1]} has author {book[2]} and read : {read}')

# Prompt add book for marking the book as read based on input name
def prompt_read_book():
    name=input("Enter the book name which u just read:")
    database4.mark_book_as_read(name)

# Prompt delete book
def prompt_delete_book():
    name=input("Enter the book name to delete:")
    database4.delete_book(name)

menu()