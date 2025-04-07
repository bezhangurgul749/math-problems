def calculate_area_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = calculate_area_rectangle(5, 3)

print("Rectangle Area: ", area, " Perimeter: ", perimeter)
