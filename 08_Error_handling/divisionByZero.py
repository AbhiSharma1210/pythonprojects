# A simple program to handle division by zero

def division(numA, numB):
    try:
        result = numA / numB
        return result
    
    except ZeroDivisionError as e:
        print(f"Error. {e}")

def main():
    try:
        userInputA, userInputB = map(int, input("Enter two space separated numbers: ").split(" "))
        
        if (division(userInputA, userInputB) != None):
            print(f"The result is: {division(userInputA, userInputB)}")
    
    except ValueError:
        print("Invalid Input. Please enter numbers only.")

if __name__ == "__main__":
    main()