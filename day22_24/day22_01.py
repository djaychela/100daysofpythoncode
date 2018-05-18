from functools import wraps
import time


def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # do something before the original function is called
        # call the passed in function
        result = function(*args, **kwargs)
        # do something after the original function call
        return result
    return wrapper


@mydecorator
def my_function(args):
    pass


def my_function(args):
    pass


my_function = mydecorator(my_function)