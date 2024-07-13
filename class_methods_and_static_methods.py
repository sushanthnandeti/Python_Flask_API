class Book():

    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, booktype, weight):
        self.name = name 
        self.booktype = booktype
        self.weight = weight 


    def __repr__(self):
        return f'<book Bookname is {self.name}, Booktype is {self.booktype} and Bookweight is {self.weight} book>'
    

    @classmethod

    def hardcover(cls, name, weight):
        return Book(name, Book.TYPES[0], weight )

    @classmethod

    def paperback(cls, name, weight):
        return Book(name, Book.TYPES[1], weight )

book = Book.hardcover('meditation', 1000)

light = Book.paperback('astrophysics for people in hurry', 600)

print(book)
print(light)
