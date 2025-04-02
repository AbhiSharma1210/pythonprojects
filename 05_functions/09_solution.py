def gen_function(number):
    for i in range(1, number, 2):
        yield i

userInput = input("Enter a number preferable greater than 5: ")
try:
    userInput = int(userInput)
    for num in gen_function(userInput):
        print(num)
except ValueError:
    print("Invalid input. Please enter a number.")