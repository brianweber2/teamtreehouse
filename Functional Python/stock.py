from copy import copy
import json
from functools import reduce, partial
from operator import attrgetter, itemgetter


class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

### SORTING ###
#pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
#print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
#pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'), reverse=True)
#print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

# important_list.sort() # Bad idea, sorts list in place
# sorted(important_list) # Sorts a copy of the list

### MAP ###
def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price - book.price*.2, 2)
    return book

#sales_books = list(map(sales_price, BOOKS))
#sales_books2 = [sales_price(book) for book in BOOKS]
#print(BOOKS[0].price)
#print(sales_books2[0].price)

### FILTER ###
def is_long_book(book):
    """Does a book have 600+ pages?"""
    return book.number_of_pages >= 600

#long_books = list(filter(is_long_book, BOOKS))
#long_books2 = [book for book in BOOKS if is_long_book(book)]
#print(len(BOOKS))
#print(len(long_books2))

### FUNCTION CHAINING ###
def has_roland(book):
    return any(["Roland" in subject for subject in book.subjects])

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

#print(list(map(titlecase, filter(has_roland, BOOKS))))
def is_good_deal(book):
    return book.price <= 5

#cheap_books = sorted(
#    filter(is_good_deal, map(sales_price, BOOKS)),
#    key=attrgetter('price')
#)
#print(cheap_books[0].price)

### REDUCE ###
def product(x, y):
    return x * y

# print(reduce(product, [1, 2, 3, 4, 5]))

### Messy code ###
#total = 0
#for x in [1, 2, 3, 4, 5]:
#    total = x * total if total else x * 1

def add_book_prices(book1, book2):
    return book1 + book2

#total = reduce(add_book_prices, [b.price for b in BOOKS])

def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None
    if a is None and b is None and books is not None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and books and books is not None and b is None:
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and b is not None and books is not None:
        return long_total(a+b, None, books)
    if a is not None and b is not None and not books:
        return long_total(a+b, None, None)
    if a is not None and b is None and not books or books is None:
        return a
#print(long_total(None, None, [b.price for b in BOOKS]))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#print(factorial(5))

### LAMBDA ###
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
good_deals = filter(lambda book: book.price <= 6, BOOKS)
#print(len(list(good_deals)))

### PARTIALS ###
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price - book.price*discount, 2)
    return book

standard = partial(mark_down, discount=0.2)
half = partial(mark_down, discount=0.5)
half_price_books = map(half, filter(is_long_book, BOOKS))
#print(half(BOOKS[0]).price)
#print(list(half_price_books))

### CURRYING ###
def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z
    
    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y, z)
    
    return lambda y, z=None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z))
    )

#print(curried_f(2, 3, 4))
#g = curried_f(2)
#print(g)
#h = g(3)
#print(h)
#i = h(4)
#print(i)