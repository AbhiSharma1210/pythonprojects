userString = input("Enter the string to reverse: ")
stringLength = len(userString)
reversedString = ""
for num in range(stringLength - 1, -1, -1): # Start from the last character and go backwards
    reversedString += userString[num]
print(f"Reversed string: {reversedString}")