def sum_all(*args):
    return sum(args)

numbers = []
numbers = input("Enter numbers separated by space: ").split()
try:
    numbers = [int(num) for num in numbers]
    result = sum_all(*numbers)
    print(f"The sum of the numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter numbers only.")