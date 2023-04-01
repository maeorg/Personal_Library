# My personal library
# SQL database: 
# - books i have
# - who i have lent them to and when

import sqlite3
from datetime import date


# Database file
database = "database.db"


class Lender():
    def __init__(self, name, info="-"):
        self.name = name
        self.info = info
        self.id = None


class Book:
    def __init__(self, title, author, publisher, language, year, genre, original_title="-", isbn="-", comments="-"):
        self.title = title
        self.original_title = original_title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.language = language
        self.genre = genre
        self.isbn = isbn
        self.comments = comments
        self.lent_out = False


    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, title):
        self._title = title


    def __str__(self):
        return "Title: " + self.title + "\nAuthor: " + self.author + "\nYear: " + self.year + \
                "\nPublisher: " + self.publisher + "\nGenre: " + self.genre + "\nLanguage: " + self.language + \
                "\nOriginal title: " + self.original_title + "\nISBN: " + self.isbn + "\nComments: " + self.comments +\
                 "\nLent out: " + str(self.lent_out)


    def return_book(self, lending_id, returned_time):
        # Update in borrowings database adding the current borrowings return time
        self.lent_out = False
        ...


def main():
    book = Book('best book ever', 'great author', 'cool publisher', 'english', '2004', 'miscellaneous')
    lender = Lender("Kalle Kant", "kollane")
    # print(book)
    # lender_id = add_lender(lender)
    # print(lender_id)
    book_id = add_book(book)
    # print(book_id)
    remove_book(book_id)
    # remove_lender(id)
    lender_id = 20
    book_id = 7
    lending_time = date.today()
    lend_book(book_id, lender_id, lending_time)


def add_book(book):
    book_as_list = [book.title, book.author, book.year, book.publisher, book.language, book.genre, \
                    book.original_title, book.isbn, book.comments, book.lent_out]
    db = connect_database(database)
    with db:
        db.execute("INSERT INTO books(title, author, year, publisher, language, genre, original_title, \
                    isbn, comments, lent_out) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", book_as_list)
        db.commit()
        book_id = db.execute("SELECT last_insert_rowid()").fetchone()
        return book_id[0]


def remove_book(id):
    db = connect_database(database)
    with db:
        db.execute("DELETE FROM books WHERE id=?", [id])


def add_lender(lender):
    db = connect_database(database)
    with db:
        db.execute("INSERT INTO lenders(name, info) VALUES(?, ?)", [lender.name, lender.info])
        db.commit()
        lender_id = db.execute("SELECT last_insert_rowid()").fetchone()
        return lender_id[0]


def remove_lender(id):
    db = connect_database(database)
    with db:
        db.execute("DELETE FROM lenders WHERE id=?", [id])


def lend_book(book_id, lender_id, lending_time):
    db = connect_database(database)
    with db:
        db.execute("INSERT INTO lending_log(book_id, lender_id, lending_time, returned_time) \
                    VALUES(?, ?, ?, ?)", [book_id, lender_id, lending_time, ""])
        db.execute("UPDATE books SET lent_out = ? WHERE id = ?", [True, book_id])
        db.commit()


# Connect to the database
def connect_database(database):
    connect = None
    try:
        connect = sqlite3.connect(database)
    except Error as e:
        print(e)
    return connect


if __name__ == "__main__":
    main()
