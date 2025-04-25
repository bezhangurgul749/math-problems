import math
from fractions import Fraction

def calculate_sum(n: int) -> float:
    """
    Calculate the sum of the first n positive integers using the formula: (n * (n + 1)) / 2.
    
    Parameters:
    n (int): The number of terms in the series to be summed. Must be a non-negative integer.

    Returns:
    float: The calculated sum of the series.
    """
    return n * (n + 1) // 2

def calculate_square(n: int) -> float:
    """
    Calculate the square of the number 'n'.
    
    Parameters:
    n (int): The number to be squared.

    Returns:
    float: The calculated square of 'n'.
    """
    return n * n

def check_operations():
    # Test case 1
    assert calculate_sum(5) == Fraction(20, 2), "Test case 1 failed"
    
    # Test case 2
    assert calculate_square(3) == Fraction(9, 1), "Test case 2 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    check_operations()
