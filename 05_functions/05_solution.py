def lambda_function(number):
    # Lambda function to calculate the cube of a number
    return number ** 3

userInput = input("Enter a number to calculate it's cube: ")
try:
    userInput = int(userInput)
    cube = lambda_function(userInput)
    print(f"The cube of {userInput} is: {cube}")
    # if userInput > 0:
    #     cube = lambda_function(userInput)
    #     print(f"The cube of {userInput} is: {cube}")
    # else:
    #     print("Please enter a positive number.")
except ValueError:
    print("Invalid input. Please enter a number.")