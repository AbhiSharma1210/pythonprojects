# Swap two numbers without a third variable

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"Before swap: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swap: a = {a}, b = {b}")
