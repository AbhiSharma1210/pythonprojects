discount = 2
price = 0
totalPeople = int(input("Please enter the number of people:"))
totalCost = 0
for people in range(totalPeople):
    userAge = int(input("Please enter your age: "))
    try:
        userAge = int(userAge)
    except:
        print("Invalid age")
        exit()
        
    price = 12 if userAge >= 18 else 8
    totalCost += price
        
movieDay = input("Please enter the day of the week: ")
if (movieDay == "Wednesday"):
    totalCost -= totalPeople * discount
    print("You get a discount of $2 per ticket. The total cost is: ", totalCost)
else:
    print("The total cost is: ", totalCost)