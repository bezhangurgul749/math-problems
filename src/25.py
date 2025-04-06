def is_perfect_square(num):
    """
    Check if a given number is a perfect square.
    
    Parameters:
    num (int): The number to check
    
    Returns:
    bool: True if num is a perfect square, False otherwise
    """
    sqrt = int(num**0.5)
    return sqrt * sqrt == num

# Example usage:
print(is_perfect_square(4))  # Output: True
print(is_perfect_square(9))  # Output: True
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(25))  # Output: False
