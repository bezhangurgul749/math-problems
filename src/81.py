def find_largest_prime_factor(n):
    """
    This function finds the largest prime factor of a given number n.
    
    :param n: Integer
    :return: Largest prime factor of n
    """
    if n <= 1:
        raise ValueError("Input must be greater than 1.")
    # Divide n by 2 to remove all even factors
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    else:
        # Now n is odd, we can skip checking the next number
        pass
    
    # Now n must be an odd integer greater than 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i
            
    # This condition is to handle the case when n becomes a prime number > 2
    if n > 2:
        largest_prime = n
    
    return largest_prime

# Example usage and check function
def test_find_largest_prime_factor():
    assert find_largest_prime_factor(13) == 7, "Test failed for input 13"
    assert find_largest_prime_factor(8) == 2, "Test failed for input 8"
    assert find_largest_prime_factor(97) == 97, "Test failed for input 97"

# Run the check function
test_find_largest_prime_factor()
