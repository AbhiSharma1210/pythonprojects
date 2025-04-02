cube = lambda userInput: userInput ** 3


userInput = input("Enter a number to calculate it's cube: ")
try:
    userInput = int(userInput)
    result = cube(userInput)
    print(f"The cube of {userInput} is: {result}")
except ValueError:
    print("Invalid input. Please enter a number.")