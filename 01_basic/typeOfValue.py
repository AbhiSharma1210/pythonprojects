# A simple program to show the type of any value enter by the user.

def typeOf(value):
    while True:
        if value.lower == True:
            type = "Boolean"
            break
        elif value.lower == False:
            type = "Boolean"
            break
        
        try:
            int_value = int(value)
            type = "Integer"
            return f"{int_value} is of type {type}"
        except ValueError:
            pass
        
        try:
            float_value = float(value)
            type = "Float"
            return f"{float_value} is of type {type}"
        except ValueError:
            break
        
    return f"{value} is of type String"
        

def main():
    userInput = input("Enter any value: ")
    print("-"*50)
    print(typeOf(userInput))
if __name__ == "__main__":
    main()