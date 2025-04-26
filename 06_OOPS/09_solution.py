"""
Class Inheritance & isinstance() function.

1. In Class Inheritance, a class can inherit attributes and methods from another class.
2. The isinstance() function checks if an object is an instance of a class or a subclass.

"""

class Car:
    registered_cars = 0 

    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        Car.registered_cars += 1 

    def full_name(self):
        return f"{self.brand} {self.name}"
    
    @property
    def total_registered_cars(self): # self keyword is not required
        return Car.registered_cars
    
    @total_registered_cars.setter
    def total_registered_cars(self, value):
        raise AttributeError("Cannot modify the total registered cars count.")
    
    @total_registered_cars.deleter
    def total_registered_cars(self):
        raise AttributeError("Cannot delete the total registered cars count.")
    
# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, name, battery_size=75):
        super().__init__(brand, name)  # Call the parent class constructor
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand} {self.name} with {self.battery_size}-kWh battery"

myTesla = ElectricCar("Tesla", "Model S", 100)
myCar = Car("Toyota", "Corolla")

print(isinstance(myTesla, ElectricCar))  # The isinstance() function will return a boolean value
print(isinstance(myTesla, Car))  
print(isinstance(myTesla, str))  

print(isinstance(myCar, ElectricCar)) # Since myCar is an instance of Car, it will return False
print(isinstance(myCar, Car))
        