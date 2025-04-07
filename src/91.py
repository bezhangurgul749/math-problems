def find_largest_prime_factor(n):
    """
    Finds the largest prime factor of a given positive integer n.
    
    Parameters:
    n (int): A positive integer greater than 1.
    
    Returns:
    int: The largest prime factor of n.
    """
    if n < 2:
        raise ValueError("Input must be greater than 1.")
    
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        n //= 2
    
    # Now, we are left with an odd number. Iterate over odd numbers starting from 3.
    max_factor = int(n ** 0.5)
    for i in range(3, max_factor + 1, 2):
        while n % i == 0:
            n //= i
            if n == 1:  # We found the largest prime factor
                return i
    
    # If no divisor was found, n is a prime number.
    return n

# Example usage:
print(find_largest_prime_factor(13))  # Output should be 3 (prime factors of 13 are 3)
