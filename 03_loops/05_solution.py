userInput = input("Enter the string: ")
userInput = list(userInput)
# print(userInput)
uniqueChar = ''
for char in userInput:
    if userInput.count(char) == 1:
        uniqueChar = char
        break
if uniqueChar != '':
    print(f"First non-repeating character is: {uniqueChar}")
else:
    print("All characters are repeating")