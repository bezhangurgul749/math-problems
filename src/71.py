import math

def calculate_surface_area(shape, dimensions):
    """
    Calculate the surface area of a given shape.
    
    Parameters:
    shape (str): The type of shape ('circle', 'square', 'triangle').
    dimensions (dict): A dictionary containing the dimensions for each dimension of the shape.

    Returns:
    float: The surface area of the shape.
    """
    if shape == "circle":
        radius = dimensions.pop("radius", 0)
        diameter = radius * 2
        return math.pi * diameter ** 2

    elif shape == "square":
        side = dimensions.pop("side", 0)
        perimeter = 4 * side
        return perimeter * side

    elif shape == "triangle":
        base = dimensions.pop("base", 0)
        height = dimensions.pop("height", 0)
        area = 0.5 * base * height
        return area

    else:
        raise ValueError(f"Unknown shape: {shape}")

# Example usage:
radius = 10
dimensions = {"radius": radius, "side": None, "base": None}
print(calculate_surface_area("circle", dimensions))
