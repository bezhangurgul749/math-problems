import math

# Function to calculate the area of a triangle given its base and height
def triangle_area(base, height):
    return 0.5 * base * height

# Function to calculate the circumference of a circle given its diameter
def circle_circumference(diameter):
    return diameter * math.pi

# Example usage:
base = 4  # base length in units
height = 3  # height of the triangle
diameter = 6  # diameter of the circle (same as the base for this example)

triangle_area_result = triangle_area(base, height)
circle_circumference_result = circle_circumference(diameter)

print("Triangle area:", triangle_area_result)
print("Circumference of the circle:", circle_circumference_result)
