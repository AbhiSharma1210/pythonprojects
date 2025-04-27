"""
Decorators

1. The decorator works as a wrapper function that adds functionality to the original function.
2. In simple terms, a decorator works like a toll on the road.
3. The decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
4. The decorator is a higher-order function that takes a function as an argument and returns a new function.

"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} function ran in {end - start} time")
        return result
    return wrapper

@timer # This is a decorator
def example_function(n):
    time.sleep(n)
    print("Example function executed")
    
example_function(2)
