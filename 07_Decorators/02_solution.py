"""
Decorator continue

"""

def argCount(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} function has {len(args)} positional arguments and {len(kwargs)} keyword arguments")
        return func(*args, **kwargs)
    return wrapper

@argCount
def example_function(a, b, c=1, d=2):
    print("Example function executed")
    
example_function(1, 2)


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.
        items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("Good Morning", greeting="Good Day")