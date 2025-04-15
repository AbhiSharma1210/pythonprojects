"""
-- Polymorphism

1. Polymorphism is the ability to present the same interface for different data types.
2. It allows methods to do different things based on the object it is acting upon.
3. In Python, polymorphism is implemented through method overriding and operator overloading.
4. Method overriding is when a subclass provides a specific implementation of a method that is already defined in its superclass.
5. Operator overloading is when we define the behavior of operators for user-defined classes.
6. Python allows us to define our own behavior for built-in operators.
7. This is done by defining special methods (also known as magic methods) in the class.
8. For example, the __add__ method is used to define the behavior of the + operator.
"""

class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
    
    def fuel_type(self):
        return "Petrol"
class ElectricCar(Car):
    def __init__(self, brand, name):
        super().__init__(brand, name)
    
    def fuel_type(self):
        return "Electric"
    
myCar = Car("Mitsubishi", "Lancer Evolution 8")
myElectricCar = ElectricCar("Tesla", "Model S")
print(myCar.fuel_type())
print(myElectricCar.fuel_type())

        