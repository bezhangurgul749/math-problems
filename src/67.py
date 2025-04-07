def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Example usage:
    >>> sum_of_squares(5)
    55
    >>> sum_of_squares(3)
    14
    
    :param n: Natural number
    :type n: int
    :return: Sum of squares of the first n natural numbers
    :rtype: int
    """
    return n * (n + 1) * (2 * n + 1) // 6

# Check function with provided data points
print(sum_of_squares(5)) == 55
print(sum_of_squares(3)) == 14
