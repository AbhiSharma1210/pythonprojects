import time

def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return f"{func.__name__} function ran in {end_time - start_time} seconds"
    return wrapper

@exec_time
def factorial(number):
    try:
        number = int(number)
        factorial_result = 1
        for i in range(1, number + 1):
            factorial_result *= i
        print(f"The factorial of {number} is {factorial_result}")
        return factorial_result
    except ValueError:
        print("Error! Please enter a valid number")
    
        

userInput = input("Enter a positive number: ")
print(F"factorial is: {factorial(userInput)}")