# import and inherit car_ignition from carClass.py file

from carClass import car_ignition

class ElectricCar(car_ignition):
    def __init__(self, brand, model, km, battery_level=100):
        super().__init__(brand, model, km)
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} is charging... Battery at {self.battery_level}%.")

    def start(self, km):
        if self.battery_level <= 0:
            print(f"{self.brand} {self.model} can't start. Battery is empty.")
        else:
            print(f"{self.brand} {self.model} is humming silently.")
            self.set_distance(km)
            self.battery_level -= km 
            
def main():
    tesla = ElectricCar("Tesla", "Model 3", 0, battery_level=10)
    tesla.start(5)
    print(f"Battery left: {tesla.battery_level}%")
    tesla.start(6)  # Should fail
    tesla.charge()
    tesla.start(10)
    print(f"Total distance driven: {tesla.get_distance()} km")

if __name__ == "__main__":
    main()