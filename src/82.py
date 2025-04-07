import math

def calculate_area(shape):
    if shape == "square":
        side = float(input("Enter the length of one side: "))
        area = side * side
        print(f"The area of the square is {area:.2f}")
    elif shape == "rectangle":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        area = width * height
        print(f"The area of the rectangle is {area:.2f}")
    else:
        raise ValueError("Invalid shape. Please choose 'square' or 'rectangle'.")
