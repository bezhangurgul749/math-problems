def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
numbers = [3, 7, 9, 15]
prime_numbers = [num for num in numbers if is_prime(num)]
print(prime_numbers)
