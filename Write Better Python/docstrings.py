def does_something(arg):
    """ Takes one argument and does something based on type.
    If arg is a string, returns arg * 3;
    If arg is an int or float, returns arg + 10
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")
