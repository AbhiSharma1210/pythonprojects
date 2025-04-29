# counting the number of function calls

def call_count(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been called {wrapper.count} times")
        return func(*args, **kwargs)
    
    wrapper.count = 0
    return wrapper

@call_count
def example_function():
    print("Example function executed")
    
example_function()
example_function()
example_function()
example_function()

