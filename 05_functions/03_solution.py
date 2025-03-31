def multiply_all(variableA, variableB):
    return variableA * variableB

userInput_A = input("Enter a string or a number: ")
userInput_B = input("Enter a number: ")
try:
    userInput_B = int(userInput_B)
    if userInput_A.isdigit():
        userInput_A = int(userInput_A)
    result = multiply_all(userInput_A, userInput_B)
    print(f"The result of multiplying {userInput_A} with {userInput_B} is {result}")
except ValueError:
    print("Please enter a valid number for the second input")