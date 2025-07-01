# A simple program to create a custon error if invalid age is entered

class InvalidAgeError(Exception):
    # Custom errors are always defined as a class
    def __init__(self, age, message="Invalid age. Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age > 0 and age < 120:
        return 1
    else:
        raise InvalidAgeError(age)
    

def main():
    try:
        userAge = int(input("Enter an age between 0 and 120: "))
        result = validate_age(userAge)
    
        if result == True:    
            print(f"Your entered age: {userAge}")
    except InvalidAgeError as e:
        print(f"{e}")

    except ValueError as e:
        print(f"Error. {e}")

if __name__ == "__main__":
    main()