def calculate_area(shape):
    if shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is {area:.2f}")
    
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * (radius ** 2)
        print(f"The area of the circle is {area:.2f}")

    else:
        print("Invalid shape")
