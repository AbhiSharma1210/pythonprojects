# A simple program to count the frequency of elements in a list

# We can use a dictionary to make key: value pair, element: count

def count_element(str):
    frequency_dict = {}
    for item in str:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return f"The frequency of each element in the entered list is \n {frequency_dict}"

def main():
    userInput = []
    print("Count the frequency of elements in a list")
    userInput = input("Enter a few elements separated by a space: ").split(" ")
    print(count_element(userInput))
    

if __name__ == "__main__":
    main()