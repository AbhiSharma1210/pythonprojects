class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
myCar = Car("Mitsubishi", "Lancer")
print(myCar.full_name())
myNewCar = Car("Mahindra", "BE69")
print(myNewCar.full_name())