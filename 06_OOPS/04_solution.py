# Encapsulation
"""
1. Encapsulation is the bundling of data with the methods that operate on that data.
2. It restricts direct access to some components and can prevent the accidental modification of data.
3. In Python, encapsulation is implemented using private and public attributes and methods.
4. Private attributes and methods are defined by prefixing the name with a double underscore (__).
"""

class Car:
    def __init__(self, brand, name):
        self.__brand = brand
        self.name = name
        # self.__number = number
    
    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.get_brand()} {self.name}"
    

myCar = Car("Mitsubishi", "Lancer Evolution 8")
print(myCar.full_name())
    

        
        