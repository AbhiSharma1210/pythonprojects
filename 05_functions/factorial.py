# A simple program to find the factorial of a number

def fact(num, result):
    if num > 1:
        result *= num - 1
        num -= 1
        return fact(num, result)
    else:
        return result
        

def main():
    print("Factorial of a number")
    userInput = input("Enter a positive number: ")
    try:
        number = int(userInput)
        if number > 0:
            print(f"Factorial of the number {number} is: ", end="")
            print(fact(number, number))
        else:
            print(f"{number} is smaller than 0. Please enter a number greater than 0.")
    except ValueError:
        print(f"{userInput} is an Invalid Input. Please try again with a valid input")

if __name__ == "__main__":
    main()