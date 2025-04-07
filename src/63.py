def sum_of_squares(x):
    """
    Calculate the sum of squares of all natural numbers up to and including x.
    
    Example usage:
    >>> sum_of_squares(5)
    55
    """
    # Sum of squares formula: n(n + 1)(2n + 1) / 6
    return (x * (x + 1) * (2 * x + 1)) // 6

# Example usage
result = sum_of_squares(7)
print(f"The sum of squares up to and including 7 is: {result}")
