def calculate_sum(numbers):
    """
    Calculate the sum of all numbers provided as an argument.
    
    Args:
    numbers (list): A list of numbers to be summed up.
    
    Returns:
    int: The sum of all numbers.
    """
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage and verification
numbers = [1, 2, 3, 4]
result = calculate_sum(numbers)
print("Sum:", result)  # Expected output: Sum: 10
