userInput = input("Enter the number: ")
evenSum = 0
try:
    userInput = int(userInput)
    for even in range(0, userInput):
        if even % 2 == 0:
            evenSum += even
    print(f"Sum of even numbers from 0 to {userInput} is {evenSum}")
except ValueError:
    print("Please enter a valid number")