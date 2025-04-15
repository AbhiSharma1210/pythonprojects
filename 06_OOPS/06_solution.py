"""
Class Variable

1. Class variables are shared among all instances of a class.
2. They are defined within the class and outside any instance methods.
3. Class variables are accessed using the class name or the instance name.
4. They are useful for storing data that is common to all instances of a class.
5. Class variables are defined using the class name followed by the variable name.
6. They can be accessed using the class name or the instance name.
7. Class variables are not tied to any specific instance of the class.

"""

class Car:
    registered_cars = 0 
    
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        Car.registered_cars += 1 
        
    def full_name(self):
        return f"{self.brand} {self.name}"
    
myCar = Car("Mitsubishi", "Lancer Evolution 8")
myCar2 = Car("Tesla", "Model S")
print(myCar.full_name())
print(myCar2.full_name())
print(f"Total registered cars: {Car.registered_cars}")  # Accessing class variable using class name
print(f"Total registered cars: {myCar.registered_cars}")  # Accessing class variable using instance name

# Example to add multiple cars
car_data = [("Toyota", "Supra"), ("Nissan", "GTR"), ("Mazda", "RX-7")]

# Creating a list of objects
cars = [Car(brand, name) for brand, name in car_data]
for car in cars:
    print(car.full_name())
print(f"Total registered cars: {Car.registered_cars}")  # Accessing class variable using class name