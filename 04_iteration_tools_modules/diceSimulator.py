import random

def dice_output(dice):
    dice_sides = {1: 6, 2: 10, 3: 16, 4: 20}
    sides = dice_sides.get(dice)
    if sides:
        output = random.randint(1, sides)
        return f"The dice rolled a... {output}"
    return "Invalid dice type."

def main():
    print("🎲 Dice Simulator")
    print("Select one of the following:")
    print("1 for a d6 dice\n2 for a d10 dice\n3 for a d16 dice\n4 for a d20 dice")
    
    try:
        user_input = int(input("Enter your choice: "))
        if 1 <= user_input <= 4:
            print(dice_output(user_input))
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()