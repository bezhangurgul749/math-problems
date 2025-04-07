def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Example:
    >>> sum_of_squares(3)
    14
    """
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

# Test the function with a sample input
result = sum_of_squares(5)
print(result)  # Output: 55
