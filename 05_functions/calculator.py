# A calculator program that takes '+', '-', '*', '/' as user inputs.

def calculate(numA, numB, symbol):
    if symbol == "+":
        return f"{numA} {symbol} {numB} = {numA + numB}"
    elif symbol == "-":
        return f"{numA} {symbol} {numB} = {numA - numB}"
    elif symbol == "*":
        return f"{numA} {symbol} {numB} = {numA * numB}"
    elif symbol == "/":
        return f"{numA} {symbol} {numB} = {numA / numB}"
    else:
        return f"Unable to recognize the symbol, please try again."

def main():
    print("Calculator")
    try:
        userInput_A, userInput_B = map(int, input("Enter 2 numbers separated by a space: ").split(" "))
        userSymbol = input("Enter the arthematic operation you want to perform +, -, *, /: ")
        print("-*-"*20)
        print(calculate(userInput_A, userInput_B, userSymbol))
    except ValueError:
        print("Invalid Input. Please enter valid numbers")
        
if __name__ == "__main__":
    main()