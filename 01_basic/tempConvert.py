# A simple program to convert Celsius to Fahrenheit

def temperature_convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    print("**Convert Celsius to Fahrenheit**")
    print("-"*30)
    userInput = input("Enter the temperature in Celsius (decimals allowed): ")
    try:
        celsius = float(userInput)
        result = temperature_convert(celsius)
        print(f"{celsius}°C equal to {result} F")
    except ValueError:
        print("Invalid input. Please try again.")
    
if __name__ == "__main__":
    main()