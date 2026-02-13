from modules import clear_screen
from library import Library
from logger import show_history
import os
library = Library()
while True:
    choice = input('What do you want to do?\n1.Manage books\n2.Manage members\n3.Borrow / Return operations\n4.Search book or member\n5.Take reports\n6.Clear screen\n7.Help\n0.Exit: ')
    if choice == '1': # manage books
        while True:
            choice = input('Manage books: What do you want to do?\n1.Add new book\n2.Edit book information\n3.Delete a book\n4.Show all books\n0.Exit: ')
            if choice == '1': # add a new book
                title = input('enter the title of book: ')
                author = input('enter the author of book: ')
                book_id = library.add_book(title, author)
                print(f'book added. ID: {book_id}')
            elif choice == '2': # edit book
                book_id = input('Enter book ID: ')
                book = library.find_book(book_id)
                if not book:
                    print('invalid id')
                    continue
                while True:
                    choice = input('What do you want to do?\n1.Edit title \n2.Edit author \n0.Exit: ')
                    if choice == '1':
                        new_title = input('Enter new title: ')
                        result = library.edit_book(book, new_title=new_title)
                        if result == "EMPTY":
                            print('your input is empty')
                        elif result == 'OK':
                            print("title changed")
                    elif choice == '2':
                        new_author = input('Enter new author: ')
                        result = library.edit_book(book, new_author=new_author)
                        if result == "EMPTY":
                            print('your input is empty')
                        elif result == 'OK':
                            print('author changed')
                    elif choice == '0':
                        break
                    else:
                        print('Enter a number between 0-2')    
            elif choice == '3': # delete a book
                book_id = input('Enter book ID: ')
                result = library.delete_book(book_id)
                if result == "NOT_FOUND":
                    print('invalid id')
                elif result == "BORROWED":
                    print('book is borrowed.')
                elif result == 'OK':
                    print('book deleted.')
            elif choice == '4': #‌ show all books
                result = library.show_books()
                if x:
                    for book in x:
                        print(book)
                else:
                    print('book list is empty.')
            elif choice == '0': # exit
                break
            else:
                print('Enter a number between 0-4')
    elif choice == '2': # manage members
        while True:
            choice = input('Manage members: What do you want to do?\n1.Add new member\n2.Edit member information\n3.Delete  member\n4.Show all members\n0.Exit: ')
            if choice == '1':  # add a member
                name = input('enter name: ')
                member_id = library.add_member(name)
                print(f'member added. ID: {member_id}')
            elif choice == '2':  # edit a member
                member_id = input('Enter member ID: ')
                member = library.find_member(member_id)
                if not member:
                    print('invalid id')
                    continue
                while True:
                    choice = input('What do you want to do?\n1.Edit name \n0.Exit: ')
                    if choice == '1':
                        new_name = input('Enter new name: ')
                        result = library.edit_member(member, new_name=new_name)
                        if result == "EMPTY":
                            print('your input is empty')
                        elif result == "OK":
                            print('name changed')
                    elif choice == '0':
                        break
                    else:
                        print('Enter a number between 0-1')
            elif choice == '3':  # delete a member
                member_id = input('Enter member ID: ')
                result = library.delete_member(member_id)
                if result == "NOT_FOUND":
                    print('invalid id')
                elif result == "HAS_BOOKS":
                    print('member has borrowed books')
                elif result == "OK":
                    print('member deleted')
            elif choice == '4':  # show members
                result = library.show_members()
                if x:
                    for member in x:
                        print(member)
                else:
                    print('member list is empty.')
            elif choice == '0':  # exit
                break
            else:
                print('Enter a number between 0-4')
    elif choice == '3': # borrowing and return
        while True:
            choice = input('Borrow / Return operations: What do you want to do?\n1.Borrow a book\n2.Return a book\n3.Show borrowed books\n4.Show available books\n0.Exit: ')
            if choice == '1': # borrow a book
                book_id = input('enter the book id: ')
                member_id = input('enter the member id: ')
                result = library.borrow_book(member_id, book_id)
                if result == "NOT_FOUND":
                    print('invalid member id or book id')
                elif result == "BORROWED":
                    print('book is borrowed already')
                elif result == "OK":
                    borrowed_books = library.member_borrowed_books(member_id)
                    print(f'Done. your books:{borrowed_books}')
            elif choice == '2': # return a book
                book_id = input('enter the book id: ')
                member_id = input('enter the member id: ')
                result = library.return_book(member_id, book_id)
                if result == "NOT_FOUND":
                    print('invalid member id or book id')
                elif result == "BOOK_AVAILABLE":
                    print('book is in library')
                elif result == "HASN'T_BOOK":
                    print('book not yours')
                elif result == "OK":
                    borrowed_books = library.member_borrowed_books(member_id)
                    print(f'Done. your books:{borrowed_books}')
            elif choice == '3': # show borrowed books
                result = library.show_borrowed_books()
                if x:
                    for book in x:
                        print(book)
                else:
                    print('borrowed list is empty')
            elif choice == '4': # show available books
                result = library.show_available_books()
                if x:
                    for book in x:
                        print(book)
                else:
                    print('available list is empty')
            elif choice == '0': # exit
                break
            else:
                print('Enter a number between 0-4')
    elif choice == '4': # search
        while True:
            choice = input('What do you want to do?\n1.Search book by title\n2.Search book by ID\n3.Search member by name\n4.Search member by ID\n0.Exit: ')
            if choice == '1': # search a book by title
                book_title = input('Enter book title: ')
                books = library.search_book_title(book_title)
                if books:
                    for book in books:
                        print(book)
                else:
                    print('book not found.')
            elif choice == '2': # search a book by ID
                book_id = input('Enter book ID: ')
                result = library.search_book_id(book_id)
                if x:
                    print(x)
                else:
                    print('Sorry, book not found, your ID is wrong.')
            elif choice == '3': # search a member by name
                member_name = input('Enter member name: ')
                members = library.search_member_name(member_name)
                if members:
                    for member in members:
                        print(member)
                else:
                    print('Member not found!')
            elif choice == '4': # search a member by ID
                member_id = input('Enter member ID: ')
                result = library.search_member_id(member_id)
                if x:
                    print(x)
                else:
                    print('Sorry, member not found, your ID is wrong.')
            elif choice == '0': # exit
                break
            else:
                print('Enter a number between 0-4')
    elif choice == '5': # generate a report
        while True:
            choice = input('What do you want to do? \n1.General report as txt \n2.Show history \n0.Exit: ')
            if choice == '1':
                library.generate_report()
                print('Done!')
            elif choice == '2':
                result = show_history()
                if x:
                    print(x)
                else:
                    print('history is empty.')
            elif choice == '0':
                break
            else:
                print('Enter a number between 0-2')
    elif choice == '6': # clear screen
        clear_screen()
    elif choice == '7': # help
        print('this program have 5 menu for library \n1.for managing books(add-edit-remove-show) \n2.for managing members(add-edit-remove-show) \n3.for borrow and return a book(borrow return available-books borrowed-books) \n4.for searching books or members based on name/title or id\n5.for take txt reports(general history)\n6.clear screen')
    elif choice == '0': # exit
        break
    else:
        print('Enter a number between 0-7')