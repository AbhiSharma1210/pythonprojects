# using Math to calculate Sq root, power and trigonometry.

import math

def squareRoot(num):
    return f"The square root of {num} is {round(math.sqrt(num), 2)}"

def power_of_number(numA, numB):
    return f"{numA} to power {numB} is {math.pow(numA, numB)}"

def trigonometry(angle):
    angle_deg = angle
    angle_rad = math.radians(angle_deg)

    return f"Sine of {angle_deg} degrees: {round(math.sin(angle_rad), 2)}"

def main():
    print("Select one of the following.")
    userInput = input("Press 1 to calculate square root. \nPress 2 to get A to power B. \nPress 3 Sine of an angle. \nEnter your choice: ")
    try:
        choice = int(userInput)
        match choice:
            case 1:
                print("-"*50)
                sqrtInput = input("Please enter a valid number to calculate the square root: ")
                try:
                    sqrtNum = int(sqrtInput)
                    print(squareRoot(sqrtNum)) 
                except ValueError as e:
                    print(f"Error. {e}")
            
            case 2:
                print("-"*50)
                try:
                    power_numA, power_numB = map(int, input("Enter number A and its power number B, separated by a space: ").split())
                    print(f"{power_of_number(power_numA, power_numB)}")
                
                except ValueError as e:
                    print(f"Error, {e}")
            
            case 3:
                print("-"*50)
                print("Enter 30, 45, 60 or 90 as an input")
                try:
                    userAngle = input("Enter the correct angle: ")
                    list_angles = [30, 45, 60, 90]
                    angle = int(userAngle)
                    if angle not in list_angles:
                        print("Incorrect input. Please enter only the specified values.")
                    else:
                        print(trigonometry(angle))
                except ValueError as e:
                    print(f"Error, {e}")

    except ValueError as e:
        print(f"Error, {e}")

if __name__ == "__main__":
    main()