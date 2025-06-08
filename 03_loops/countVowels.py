# count the number of Vowels in a given string using for loop.

def count_vowels(userStr):
    vowels = {"a", "e", "i", "o", "u"}
    countVowel = 0
    for char in userStr.lower():
        if char in vowels:
            countVowel += 1
    return countVowel

# an even shorter version of this is 
def count_vowels2(userStr):
    return sum(1 for char in userStr.lower() if char in "aeiou")
        
    

def main():
    print("Count the number of Vowels in a string")
    userInput = input("Enter any string: ")
    print("-"*50)
    print(f"The number of vowels in the given string is {count_vowels(userInput)} \n")

if __name__ == "__main__":
    main()