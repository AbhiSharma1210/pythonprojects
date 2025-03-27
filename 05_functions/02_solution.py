def addition(first_number, second_number):
    return first_number + second_number

userInput = input("Enter two numbers separated by a space: ")
try:
    numbers = userInput.split()
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    sum = addition(first_number, second_number)
    print(f"The sum of {first_number} and {second_number} is {sum}")
except ValueError:
    print("Please enter two valid numbers separated by a space")