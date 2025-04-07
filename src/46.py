def find_largest_prime_factor(n):
    """
    This function calculates the largest prime factor of a given number n.
    
    Parameters:
    n (int): The number to find the largest prime factor of
    
    Returns:
    int: The largest prime factor of n
    """
    # Divide n by 2 to get rid of all even factors
    while n % 2 == 0:
        largest_prime_factor = 2
        n //= 2
        
    # Now, we are left with odd factors.
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime_factor = i
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        largest_prime_factor = n
        
    return largest_prime_factor

# Example usage:
number = 13195
largest_prime = find_largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {largest_prime}")
