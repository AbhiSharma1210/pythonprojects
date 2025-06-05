# A simple calculator application

def add_num(numA, numB):
    return numA + numB

def sub_num(numA, numB):
    return numA - numB

def multi_num(numA, numB):
    return numA * numB

def div_num(numA, numB):
    return numA / numB

def main():
    print("Simple Calculator\n")
    print("Enter 1 to add two numbers.")
    print("Enter 2 to subtract two numbers.")
    print("Enter 3 to multiply two numbers.")
    print("Enter 4 to divide two numbers.")
    print("Enter 5 to exit")
    
    userChoice = input("\nEnter your choice: ")
    if userChoice == '5':
        return
    else:
        try:
            numberA = input("Enter number A: ")
            numberB = input("Enter number B: ")
            numA = int(numberA)
            numB = int(numberB)
        except ValueError:
            print("Invalid input please enter only numbers")
            return
        match userChoice:
            case "1":
                sum = add_num(numA, numB)
                print("-" * 25)
                print(f"The sum of the numbers {numA} and {numB} is {sum}")
            case "2":
                diff = sub_num(numA, numB)
                print("-" * 25)
                print(f"The result of subtraction between the numbers {numA} and {numB} is {diff}")
            case "3":
                multi = multi_num(numA, numB)
                print("-" * 25)
                print(f"The result of multiplication between the numbers {numA} and {numB} is {multi}")
            case "4":
                if numB == 0:
                    print("Cannot divide by zero.")
                    return
                result = div_num(numA, numB)
                print("-" * 25)
                print(f"The division of {numA} by {numB} is {result}")
            case _:
                print("Invalid option.")
                
        
            

if __name__ == "__main__":
    main()