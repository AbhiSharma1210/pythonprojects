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