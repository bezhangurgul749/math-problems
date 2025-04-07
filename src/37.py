import math

def calculate_area(shape):
    if shape == "rectangle":
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area}")
    elif shape == "triangle":
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")
    else:
        print("Invalid shape. Please enter 'rectangle' or 'triangle'.")
