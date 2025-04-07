def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input("Enter the radius: "))
print(f"The area of the circle with radius {radius} is {calculate_area(radius)}")
