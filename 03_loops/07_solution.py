while(1):
    userInput = input("Enter the number: ")
    try:
        userInput = int(userInput)
        if userInput > 1 and userInput < 10:
            print("You have entered the correct number")
            break
        else:
            print("Re-enter the number")
    except ValueError:
        print("Please enter a number. Alphabets and special characters are not allowed")
        continue

