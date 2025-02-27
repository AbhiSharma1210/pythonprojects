userInput = input("Enter the year: ")
try:
    userInput = int(userInput)
    if userInput % 4 == 0:
        if userInput % 100 == 0:
            if userInput % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
        
except ValueError:
    print("Please enter a valid year")
    