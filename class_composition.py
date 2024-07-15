class Book:

    def __init__(self, name):
        self.name = name 


    def __str__(self):
        return f'Name of the book is {self.book}'
    

class Bookshelf():

    def __init__(self, *books):
        self.books = books 

    def __str__(self):
        return f'The number of books in the bookshelf is {len(self.books)}'
    

Book1 = Book('Meditations')
Book2 = Book('Astrophysics for people in hurry')

shelf = Bookshelf(Book1, Book2)

print(shelf)