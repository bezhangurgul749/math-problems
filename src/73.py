import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse in a right triangle with sides a and b.
    
    Parameters:
    a (float): The length of side a.
    b (float): The length of side b.

    Returns:
    float: The length of the hypotenuse.
    """
    c = math.sqrt(a**2 + b**2)
    return c

# Example usage
hypotenuse = calculate_hypotenuse(3, 4)
print(hypotenuse)  # Output: 5.0
