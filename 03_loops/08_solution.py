import math
userInput = input("Enter a number: ")
try:
    userInput = int(userInput)
    for num in range(2, int(math.sqrt(userInput)) + 1):
        # The above line is optimzed to reduce the time complexity which becomes O(sqrt(n)) instead of O(n).
        if userInput % num == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
except ValueError:
    print("Please enter a valid number")
