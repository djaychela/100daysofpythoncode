from functools import wraps


def my_decorator(func):
    '''Decorator to double the value of input args.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before func
        print(f'pre-decorator args: {args}')
        arg_2 = []
        for arg in args:
            arg_2.append(arg*2)
        args = tuple(arg_2)
        func(*args, **kwargs)
        # do stuff after func
        print(f'decorator post-function - {args}')
    return wrapper


@my_decorator
def some_function(*args):
    '''Test function to print out info from args...'''
    print(f'hello, function here. values = {args}')


if __name__ == "__main__":
    some_function(6,7,4)
print(help(some_function))
print(help(my_decorator))