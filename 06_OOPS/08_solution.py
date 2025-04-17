"""
Property Decorator:

1. Property decorators are used to define properties in a class.
2. They allow you to define methods that can be accessed like attributes.
3. Property decorators are defined using the @property decorator.
4. They are useful for creating read-only or computed attributes.
5. Property decorators can also be used to define setter and deleter methods.
6. Setter methods are defined using the @property_name.setter decorator.
7. Deleter methods are defined using the @property_name.deleter decorator.
8. Property decorators provide a way to encapsulate data and control access to it.
9. They are useful for implementing data validation and encapsulation.

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

myCar = Car("Mitsubishi", "Lancer Evolution 8")
myCar2 = Car("Tesla", "Model S")
print(myCar.full_name())
print(myCar2.full_name())
print(f"Total registered cars: {Car.registered_cars}")  # Accessing class variable using class name
print(f"Total registered cars: {myCar.total_registered_cars}")  # Accessing static method using instance name