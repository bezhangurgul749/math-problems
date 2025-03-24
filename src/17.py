import numpy as np
import pandas as pd

def calculate_square_root(values):
    """
    Calculate the square root of each value in the given list.
    
    Parameters:
    values (list): A list of numerical values.

    Returns:
    list: A list containing the square roots of the input values.
    """
    return [np.sqrt(value) for value in values]

# Example usage
values = [8, 16, 25]
result = calculate_square_root(values)
print(result)
