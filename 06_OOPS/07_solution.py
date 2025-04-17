"""
Static Methods:

1. Static methods are methods that belong to the class rather than any instance of the class.
2. They do not require an instance of the class to be called.
3. Static methods are defined using the @staticmethod decorator.
4. They can be called using the class name or an instance of the class.
5. Static methods do not have access to the instance (self) or class (cls) variables.
6. They are used for utility functions that do not require access to instance or class variables.

"""

class Car:
    registered_cars = 0 

    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        Car.registered_cars += 1 

    def full_name(self):
        return f"{self.brand} {self.name}"

    @staticmethod
    def total_registered_cars(): # self keyword is not required
        return Car.registered_cars
    
myCar = Car("Mitsubishi", "Lancer Evolution 8")
myCar2 = Car("Tesla", "Model S")
print(myCar.full_name())
print(myCar2.full_name())
print(f"Total registered cars: {Car.total_registered_cars()}")  # Accessing static method using class name
print(f"Total registered cars: {myCar.total_registered_cars()}")  # Accessing static method using instance name

