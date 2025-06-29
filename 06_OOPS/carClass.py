# Classes 

class car_ignition():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.km = 0
        self.total_distance = 0

    def start(self, km):
        print("Car is running.")
        self.set_distance(km)
        
    def set_distance(self, km):
        self.total_distance += km
    
    def stop(self):
        print("Car has stopped")
    
    def get_distance(self):
        return self.total_distance

    

def main():
    car = car_ignition("Hyundai", "Exter")
    km = 0
    print("You are in the car.")
    key_ignition = False
    userInput = input("Do you want to start the car ? y/n: ")
    if userInput.lower() == 'y':
        key_ignition = True
    elif userInput.lower() == 'n':
        print("Car not started.")
    else:
        print("Invalid input. Please try again.")
    while key_ignition:
        km = 2
        car.start(km)
        print(f"You travelled {km} km.")
        userInput = input("Do you want to continue? y/n: ")
        if userInput.lower() == 'n':
            key_ignition = False
            print(f"Total distance travelled is {car.get_distance()} km")
        else:
            continue
            
        
    

if __name__ == "__main__":
    main()