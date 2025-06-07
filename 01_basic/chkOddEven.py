# A simple program to check whether a number is odd or ever

def odd_even(value):
    if (value % 2) == 0:
        return f"{value} is an Even number\n"
    else:
        return f"{value} is an Odd number\n"

def main():
    print("Check if a number is Odd or Even")
    userInput = input("Enter the number: ")
    try:
        value = int(userInput)
        print("-"*50)
        print(odd_even(value))
    except ValueError:
        print("Invalid input. Please enter a valid number")

if __name__ == "__main__":
    main()