def circle(radius):
    pi = 3.1415
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    # returning the trimmed values upto 2 decimal places
    area = round(area, 2)
    circumference = round(circumference, 2)
    return area, circumference

radius = input("Enter the radius of the circle: ")
try:
    radius = float(radius)
    if radius > 0:
        (circle_area, circle_circumference) = circle(radius)
        print(f"Area of the circle: {circle_area}, Circumference of the circle: {circle_circumference}")
    else:
        print("Please enter a positive number for the radius.")
except ValueError:
    print("Invalid input. Please enter a number.")