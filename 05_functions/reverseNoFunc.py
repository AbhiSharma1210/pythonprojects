# Do the reverse of a list without using any in-build functions.

def reverse(list_of_numbers):
    reversed_list = []
    for i in range(len(list_of_numbers) - 1, -1, -1):
        reversed_list.append(list_of_numbers[i])
    return reversed_list

def main():
    print("Reverse of a list of numbers")
    user_list = []
    user_list = input("Enter a few numbers separater by a space: ").split(" ")
    print("-"*50)
    print(f"You have entered the following list: \n {user_list}")
    print("\n The reversed list is: ")
    print(reverse(user_list))

if __name__ == "__main__":
    main()