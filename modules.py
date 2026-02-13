import uuid
import os
class Book:
    def __init__(self, title, author, book_id=None, is_borrowed=None):
        self.title = title
        self.author = author
        if book_id is None:
            self.book_id = str(uuid.uuid4())[:8]
        else:
            self.book_id = book_id
        if is_borrowed is None:
            self.__is_borrowed = False
        else:
            self.__is_borrowed = is_borrowed

    def __repr__(self):
        status = "borrowed" if self.__is_borrowed else "available"
        return f"[{self.book_id}] {self.title} - {self.author} ({status})"

    def __str__(self):
        status = "borrowed" if self.__is_borrowed else "available"
        return f"[{self.book_id}] {self.title} - {self.author} ({status})"

    def change_status(self, status:bool):
        self.__is_borrowed = status
    
    def is_borrowed(self):
        return self.__is_borrowed

    def to_dict(self):
        return {
            'title' : self.title,
            'author' : self.author,
            'book_id' : self.book_id,
            'is_borrowed' : self.__is_borrowed
        }


class Member:
    def __init__(self, name,member_id=None, borrowed_books=None):
        self.name = name
        if member_id is None:
            self.member_id = str(uuid.uuid4())[:8]
        else:
            self.member_id = member_id
        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = borrowed_books

    def __repr__(self):
        return f"{self.name} [{self.member_id}] borrowed_books: {self.borrowed_books}"

    def __str__(self):
        return f"{self.name} [{self.member_id}] borrowed_books: {self.borrowed_books}"

    def to_dict(self):
        return {
            'name' : self.name,
            'member_id' : self.member_id,
            'borrowed_books' : self.borrowed_books
        } 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')