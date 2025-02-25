userAge = input("Please enter your age: ")

# try catch method to handle invalid age input
try:
    userAge = int(userAge)
except:
    print("Invalid age")
    exit()
    
if (userAge < 0 or userAge > 100):
    print("Invalid age")
else:
    if (userAge < 13):
        print("The person is a Child")
    elif (userAge < 19):
        print("The person is a Teenager")
    elif (userAge >= 20):
        print("The person is an Adult")
    elif (userAge >= 60):
        print("The person is a Senior Citizen") 
    
