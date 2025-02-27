userPassword = input("Enter your password: ")
passLength = len(userPassword)
alphabets = 0
numbers = 0
specialChars = 0
if passLength < 6:
    print("Password is weak")
elif passLength < 10:
    print("Password strength is medium")
else:
    print("Password is strong")
    
for char in userPassword:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        numbers += 1
    else:
        specialChars += 1
    
if alphabets > 0 and numbers > 0 and specialChars > 0:
    print("You have used a combination of alphabets, numbers and special characters")
elif alphabets > 0 and numbers > 0:
    print("You have used a combination of alphabets and numbers")
elif alphabets > 0 and specialChars > 0:
    print("You have used a combination of alphabets and special characters")
elif numbers > 0 and specialChars > 0:
    print("You have used a combination of numbers and special characters")
elif alphabets > 0:
    print("You have used only alphabets")
elif numbers > 0:
    print("You have used only numbers")
else:
    print("You have used only special characters")