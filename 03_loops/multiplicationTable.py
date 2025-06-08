# A simple program to print the multiplication table of any number.

def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")
    return

def main():
    print("Multiplication table")
    userInput = input("Enter a number: ")
    try:
        number = int(userInput)
        print_table(number)
    
    except ValueError:
        print(f"{userInput} is not a valid input. Please try again")
    
if __name__ == "__main__":
    main()