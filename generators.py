# generators


def plus1(x):
    """
    takes a value and adds 1 to it
    """
    return x + 1


def mymap(func, iterable):
    """
    takes a list of values and applies the given function to each value
    """
    print("hello world")
    for x in iterable:
        yield func(x)
    print("goodbye shafan")
