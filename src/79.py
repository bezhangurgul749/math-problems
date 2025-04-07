def sum_of_squares(n):
    """
    Calculate the sum of squares of numbers from 1 to n.
    
    Parameters:
    n (int): The upper limit of the range.

    Returns:
    int: The sum of squares from 1 to n.
    """
    return sum(i ** 2 for i in range(1, n + 1))

# Example usage
print(sum_of_squares(5))  # Output: 55
