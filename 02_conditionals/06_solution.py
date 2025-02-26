userInput = input("Enter the distance to travel: ")
distance = int(userInput)
if distance > 0:
        if distance < 3:
            print("Walk")
        elif distance < 15:
            print("Use a Bicycle")
        else:
            print("Use a Car")
else:
    print("Please enter a valid number")