import math

def calculate_area(shape):
    if shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of {shape} is: {area:.2f}")
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = math.pi * (radius ** 2)
        print(f"The area of a circle with radius {radius} is: {area:.2f}")
    else:
        print("Invalid shape. Please choose 'rectangle' or 'circle'.")

calculate_area("rectangle")
