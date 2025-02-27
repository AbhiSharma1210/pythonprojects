coffeeSize = ("Small", "Medium", "Large")
extraOption = ("Extra shot")
userInput = input("What size coffee would you like? 1. Small 2. Medium 3. Large \nEnter the number: ")
userInput = int(userInput)
userOption = input("Would you like an extra shot? (yes/no) ")
if userInput == 1:
    if userOption == "yes":
        print(f"You have selected a {coffeeSize[0]} coffee with an {extraOption[0]}")
    else:
        print(f"You have selected a {coffeeSize[0]} coffee with No extra shot selected")
elif userInput == 2:
    if userOption == "yes":
        print(f"You have selected a {coffeeSize[1]} coffee with an {extraOption[0]}")
    else:
        print(f"You have selected a {coffeeSize[1]} coffee with No extra shot selected")
elif userInput == 3:
    if userOption == "yes":
        print(f"You have selected a {coffeeSize[2]} coffee with an {extraOption[0]}")
    else:
        print(f"You have selected a {coffeeSize[2]} coffee with No extra shot selected")
else:
    print("Invalid input")