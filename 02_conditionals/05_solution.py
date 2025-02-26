userInput = input("Enter the weather today: ")
weather = {"Sunny": "Go for a walk", "sunny": "Go for a walk", "Rainy": "Read a book", "rainy": "Read a book", "Snowy": "Build a snowman", "snowy": "Build a snowman"}
if userInput in weather:
    print(weather[userInput])
else:
    print("I've no suggestion for that weather")