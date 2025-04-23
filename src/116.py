import sympy as sp
import numpy as np

def find_largest_prime_factor(num):
    """
    Find the largest prime factor of a given number.
    
    Parameters:
    - num: An integer representing the number to be analyzed
    
    Returns:
    - The largest prime factor of the input number
    """
    if num < 2:
        raise ValueError("Input number must be greater than or equal to 2")
    for i in range(2, int(np.sqrt(num)) + 1):
        while (num % i == 0):
            largest_prime_factor = i
            break
    return largest_prime_factor

# Example usage:
input_number = 60
largest_prime_factor = find_largest_prime_factor(input_number)
print(f"The largest prime factor of {input_number} is: {largest_prime_factor}")
