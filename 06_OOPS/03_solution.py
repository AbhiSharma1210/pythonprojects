class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size} kWh"
    

myCar = ElectricCar("Tesla", "Model S", 100)
print(myCar.full_name())