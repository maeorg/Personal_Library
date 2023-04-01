# My personal library
# (CSV?) SQL database: 
# - books i have
# - who i have lent them to and when

import sqlite3


# Database file
database = "database.db"


class Borrower():
    def __init__(self, name, contact_info="-"):
        self.name = name
        self.contact_info = contact_info


class Book:
    def __init__(self, title, author, publisher, year, genre, original_title="-", isbn="-", comments="-"):
        self.title = title
        self.original_title = original_title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.isbn = isbn
        self.comments = comments


    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, title):
        self._title = title


    def __str__(self):
        return "Title: " + self.title + "\nAuthor: " + self.author + "\nYear: " + self.year + \
                "\nPublisher: " + self.publisher + "\nGenre: " + self.genre + "\nOriginal title: " \
                 + self.original_title + "\nISBN: " + self.isbn + "\nComments: " + self.comments



def main():
    book = Book('best book ever', 'great author', 'cool publisher', '2004', 'miscellaneous')
    print(book)
    book.title = "hey"
    print(book.title)


if __name__ == "__main__":
    main()
