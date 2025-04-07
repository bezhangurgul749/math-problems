# Problem: Find the maximum value of the function f(x) = x^2 - 4x + 3

import numpy as np

def find_max_value():
    # Define the function f(x)
    def f(x):
        return x**2 - 4*x + 3
    
    # Find the maximum value using numerical optimization
    max_value, max_x = np.max(f(np.linspace(-10, 10, 100)), axis=0)
    
    return max_value, max_x

# Find the maximum value and its corresponding x-value
max_val, max_x = find_max_value()
print("Maximum value:", max_val)
print("X-coordinate of maximum value:", max_x)
