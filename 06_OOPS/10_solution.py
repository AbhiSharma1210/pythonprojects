"""
# Multiple Inheritance

1. In Multiple Inheritance, a class can inherit from multiple classes.
2. The super() function is used to call methods from a parent class.
3. The MRO (Method Resolution Order) determines the order in which classes are searched when calling a method.
4. The super() function can be used to call methods from parent classes in the MRO.
5. The __mro__ attribute shows the MRO of a class.
6. The mro() method returns the MRO of a class.
7. The super() function can be used to call methods from parent classes in the MRO.

"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size
        
    def battery(self):
        return f"{self.battery_size} KwH"

class Engine:
    def __init__(self,engine_power=1500):
        self.engine_power = engine_power
    
    def engine(self):
        return f"{self.engine_power} HP"
    
class ElectricCar(Battery, Engine):
    def __init__(self, brand, model, battery_size=100, engine_power=1500):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)
        Engine.__init__(self, engine_power)
    
    def full_name(self):
        return f"{self.brand} {self.model} with {self.battery_size}-kWh battery and {self.engine_power} HP engine"


mybatt = Battery()
print(mybatt.battery())

myengine = Engine()
print(myengine.engine())

myElectricCar = ElectricCar("Tesla", "Model S", 100, 1500)
print(myElectricCar.full_name())