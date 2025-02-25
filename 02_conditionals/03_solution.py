marks = input("Enter your marks between 0 - 100: ")
try:
    marks = int(marks)
except:
    print("Invalid marks")
    exit()
    
if (marks > 100 or marks < 0):
    print("Invalid marks")
    exit()
elif (marks >= 90):
    print("You got an A")
elif (marks >= 80):
    print("You got a B")
elif (marks >= 70):
    print("You got a C")
elif (marks >= 60):
    print("You got a D")
else:
    print("You got an F")