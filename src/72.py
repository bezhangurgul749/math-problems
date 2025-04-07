import math

def calculate_cube_volume(side_length):
    """
    Calculate the volume of a cube given its side length.
    
    Args:
        side_length (float): The length of a side of the cube.
        
    Returns:
        float: The volume of the cube.
    """
    return side_length ** 3

# Example usage
cube_side = 5.0
volume = calculate_cube_volume(cube_side)
print(f"The volume of the cube with side length {cube_side} is {volume:.2f}")
