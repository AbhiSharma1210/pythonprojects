def calculate_square(number):
    return number * number

userInput = input("Enter a positive number: ")
try:
    number = int(userInput)
    square = calculate_square(number)
    print(f"The square of {number} is {square}")
except ValueError:
    print("Please enter a valid number")
        