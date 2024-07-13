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



### Exercise

class Store:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    
    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        
        return Store(store.name + " - franchise")
    
    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        TOTAL = int(Store.stock_price(store))
        return f'{store.name}, total stock price: {TOTAL}'
