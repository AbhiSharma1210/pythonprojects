# A simple program to implement the fabonacci series

def fabo(numA, numB, final):
    next_digit = numA + numB
    if next_digit < final:
        print(f" {next_digit}", end="")
        return fabo(numB, next_digit, final)
    else:
        return
        

def main():
    print("**Fabonacci Series**")
    print("-"*50)
    userInput = input("Enter a number: ")
    try: 
        lastDigit = int(userInput)
        if lastDigit > 0:
            numA = 0
            numB = 1
            print(f"Fabonacci Series till number {lastDigit} is: \n {numA} {numB}", end="")
            fabo(numA, numB, lastDigit)
        else:
            print("Please enter a number greater than 1")
    except ValueError:
        print("Invalid Input! please enter a valid number")
    print("\n")
        
if __name__ == "__main__":
    main()