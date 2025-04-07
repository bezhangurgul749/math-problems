import math

def calculate_surface_area(shape):
    """
    Calculate the surface area of a given 3D shape.
    
    Args:
        shape (str): The type of 3D shape ('cube', 'sphere', 'cylinder', etc.).
        
    Returns:
        float: The surface area of the specified 3D shape.
    """
    if shape.lower() == "cube":
        return 6 * math.pow(side_length, 2)
    
    elif shape.lower() == "sphere":
        radius = side_length / (2 * math.pi)
        return 4 * math.pi * radius ** 2
    
    elif shape.lower() == "cylinder":
        height = side_length
        radius = side_length / (2 * math.tan(math.acos(side_length / (2 * height))))
        return 2 * math.pi * radius ** 2 + math.pi * side_length * height

# Example usage:
cube_side = 5
sphere_radius = 3
cylinder_height = 10

surface_area_cube = calculate_surface_area("cube")
surface_area_sphere = calculate_surface_area("sphere")
surface_area_cylinder = calculate_surface_area("cylinder")

print(f"Surface area of a cube with side length {cube_side}: {surface_area_cube:.2f}")
print(f"Surface area of a sphere with radius {sphere_radius}: {surface_area_sphere:.2f}")
print(f"Surface area of a cylinder with height {cylinder_height} and radius: {surface_area_cylinder:.2f}")
