userInput = input("Enter the number: ")
try:
    userInput = int(userInput)
    for num in range(1, 11):
        if num != 5:
            print(f"{userInput} * {num} = {userInput * num}")
        else:
            print("Skipping 5")
except ValueError:
    print("Please enter a valid number")
