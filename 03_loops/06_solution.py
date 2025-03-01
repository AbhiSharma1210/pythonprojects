userInput = input("Enter the number: ")
factorial = 1
try:
    userInput = int(userInput)
    if userInput < 0:
        raise ValueError
    elif userInput == 0:
        print(f"Factorial of {userInput} is 1")
    else:
        num = userInput
        while num > 0:
            factorial *= num
            num -= 1
        print(f"Factorial of {userInput} is {factorial}")
except ValueError:
    print("Please enter a positive integer greater than or equal to 0")