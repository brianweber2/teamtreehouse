from functools import wraps

# nested function
def outer():
    number = 5

    def inner():
        print(number)

    inner()


# First-class functions
def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

# print(apply(add, 5, 5))
# print(apply(sub, 2, 8))


# Closure
def close():
    x = 5
    def inner():
        print(x)
    return inner


def add_to_five(num):
    def inner():
        print(num+5)
    return inner


# fifteen = add_to_five(10)
# fifteen()


# Decorators
def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner


@logme
def sub(x, y):
    """Returns the difference between two numbers"""
    return x - y
