# A simple program to find the largest of the three numbers

def find_larger(numA, numB, numC):
    if numA > numB:
        if numA > numC:
            return numA
        else:
            return numC
    elif numB > numC:
        return numB
    else:
        return numC

def main():
    print("Find the larger among the two numbers: ")
    try:
        valueA, valueB, valueC = map(int, input("Enter the three numbers separated by a space: ").split(" "))
    except ValueError:
        print("Invalid input. Please enter exactly 3 numbers separated by a space")
    print(f"The larger amoung {valueA}, {valueB} and {valueC} is {find_larger(valueA, valueB, valueC)}")

if __name__ == "__main__":
    main()