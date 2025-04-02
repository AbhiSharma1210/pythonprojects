def greet_user(name):
    print(f"Hello, {name}")

userInput = input("Enter the name or skip: ")
default_name = "Someone"
if userInput != "":
    greet_user(userInput)
else:
    greet_user(default_name)