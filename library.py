from storage import save_data, load_data, data_dir
from modules import Book, Member
from logger import save_txt, read_txt
import os
from datetime import datetime
class Library:
    def __init__(self):
        self.books = load_data('books.json', Book)
        self.members = load_data('members.json', Member)
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        save_data(self.books, 'books.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] BOOK_ADDED id={book.book_id} title="{book.title}" author="{book.author}"')
        return book.book_id
    def delete_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            return "NOT_FOUND"
        elif book.is_borrowed():
            return "BORROWED"
        self.books.remove(book)
        save_data(self.books, 'books.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] BOOK_DELETED id={book.book_id} title="{book.title}"')
        return "OK"
    def edit_book(self, book, new_author=None, new_title=None):
        if book is None:
            return "NOT_FOUND"
        changes = []
        old_title, old_author = book.title, book.author
        if new_author is None and new_title is None:
            return "EMPTY"
        if new_title is not None:
            if new_title.strip() == "":
                return "EMPTY"
            book.title = new_title
            changes.append(f'title="{old_title} "-> "{book.title}"')
        if new_author is not None:
            if new_author.strip() == "":
                return "EMPTY"
            book.author = new_author
            changes.append(f'author="{old_author}" -> "{book.author}"')
        change_text = ' | '.join(changes)
        save_data(self.books, 'books.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] BOOK_EDITED id={book.book_id} {change_text}')
        return "OK"                
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        save_data(self.members, 'members.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] MEMBER_ADDED id={member.member_id} name="{member.name}"')
        return member.member_id
    def delete_member(self, member_id):
        member = self.find_member(member_id)
        if member is None:
            return "NOT_FOUND"
        elif member.borrowed_books:
            return "HAS_BOOKS" 
        self.members.remove(member)
        save_data(self.members, 'members.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] MEMBER_DELETED id={member.member_id} name="{member.name}"')
        return "OK" 
    def edit_member(self, member, new_name):
        if member is None:
            return "NOT_FOUND"
        if new_name is None:
            return "EMPTY"
        old_name = member.name
        if new_name is not None:
            if new_name.strip() == "":
                return "EMPTY"
        member.name = new_name
        save_data(self.members, 'members.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] MEMBER_EDITED id={member.member_id} name="{old_name}" -> "{member.name}"')
        return "OK"
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member is None or book is None:
            return "NOT_FOUND"
        elif book.is_borrowed():
            return "BORROWED"
        book.change_status(True)
        member.borrowed_books.append(book.book_id)
        save_data(self.books, 'books.json')
        save_data(self.members, 'members.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] BORROW member={member.member_id} book={book.book_id}')
        return "OK"
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member is None or book is None:
            return "NOT_FOUND"
        elif book.is_borrowed() is False:
            return "BOOK_AVAILABLE"
        elif not book_id in self.member_borrowed_books(member_id):
            return "HASN'T_BOOK"
        book.change_status(False)
        member.borrowed_books.remove(book.book_id)
        save_data(self.books, 'books.json')
        save_data(self.members, 'members.json')
        save_txt('history.txt', f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}] RETURN member={member.member_id} book={book.book_id}')
        return "OK"


    def search_book_title(self, book_title):
        books = []
        query = book_title.casefold().replace(' ', '')
        for book in self.books:
            if query in book.title.casefold().replace(' ', ''):
                books.append(book)
        return books
    def search_book_id(self, book_id):
        found_book = self.find_book(book_id)
        return found_book
    def search_member_name(self, member_name):
        members = []
        query = member_name.casefold().replace(' ', '')
        for member in self.members:
            if query in member.name.casefold().replace(' ', ''):
                members.append(member)
        return members
    def search_member_id(self, member_id):
        found_member = self.find_member(member_id)
        return found_member


    def generate_report(self):
        book_list = self.books
        member_list = self.members
        with open(f'{data_dir}report.txt', 'w', encoding='utf-8') as report:
            report.write('Books:\n')
            for book in book_list:
                report.write(f'{repr(book)}\n')
            report.write('Members:\n')
            for member in member_list:
                report.write(f'{repr(member)}\n')

    def show_books(self):
        return self.books
    def show_members(self):
        return self.members
    def show_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed()]
    def show_available_books(self):
        return [book for book in self.books if not book.is_borrowed()]


    def member_borrowed_books(self, member_id):
        member = self.find_member(member_id)
        if member:
            return member.borrowed_books
        else:
            return []