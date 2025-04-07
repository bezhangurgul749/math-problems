def find_prime_factors(n):
    factors = []
    # Check for number 2 first because any even number greater than 2 can be factored out
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Start checking odd numbers from 3 onwards
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)

    return factors

# Example usage
print(find_prime_factors(28)) # Output: [2, 2, 7]
