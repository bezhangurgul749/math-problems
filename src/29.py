import math

def find_primes(n):
    """
    Find all prime numbers up to n.
    
    Args:
    n (int): The upper limit for finding primes.
    
    Returns:
    list: A list of prime numbers up to n.
    """
    if n <= 1:
        return []
    sieve = [True] * n
    s = int(math.sqrt(n))
    for i in range(2, s + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    primes = [i for i in range(s+1) if sieve[i]]
    return primes

# Example usage:
num = int(input("Enter an integer: "))
print(find_primes(num))
