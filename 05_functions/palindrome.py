# A simple program to find that the string is palindrome or not

def check_palindrome(str):
    new_str = str.lower().replace(" ", "")
    return new_str == new_str[::-1]

def main():
    print("Check if string is palindrome or not")
    userInput = input("Enter any string: ")
    palindrome = check_palindrome(userInput)
    if palindrome:
        print(f"{userInput} is a palindrome")
    else:
        print(f"{userInput} is not a palindrome")

if __name__ == "__main__":
    main()