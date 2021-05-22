from utils import database3
"""
adding comments
This is the background ! ***
"""

USER_CHOICE = """
- 'a' to add a book
- 'l' to list all books
- 'd' to delete a book
- 'r' to mark read a book
- 'q' to quit
Your choice:"""


def menu():
    database3.create_book_table()
    user_input= input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif  user_input == 'l':
            prompt_list_book()
        elif  user_input == 'd':
            prompt_delete_book()
        elif user_input == 'r':
            prompt_read_book()
        else:
            print("unknown command. Please try again")
        user_input=input(USER_CHOICE)


# Prompt add book for adding the book name and author
def prompt_add_book():
    name=input("Enter the book name:")
    author=input("Enter the author name")
    database3.add_book(name,author)


# Prompt add book for listing all the book name and author
def prompt_list_book():
    books=database3.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, read : {read}")

# Prompt add book for marking the book as read based on input name


def prompt_read_book():
    name=input("Enter the book name which u just read:")
    database3.mark_book_as_read(name)


# Prompt delete book
def prompt_delete_book():
    name=input("Enter the book name to delete:")
    database3.delete_book(name)


menu()
