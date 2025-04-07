def find_sum_of_odd_numbers(start: int, end: int) -> int:
    """
    This function calculates the sum of all odd numbers between the start and end parameters (inclusive).
    
    :param start: The starting number of the range.
    :param end: The ending number of the range.
    :return: The sum of all odd numbers in the given range.
    """
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    return total

# Example usage:
print(find_sum_of_odd_numbers(5, 8)) # Output: 9
