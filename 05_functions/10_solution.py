# Example of a recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

userInput = input("Enter a number to calculate its factorial: ")
try:
    userInput = int(userInput)
    if userInput < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(userInput)
        print(f"The factorial of {userInput} is: {result}")
except ValueError:
    print("Invalid input. Please enter a number.")