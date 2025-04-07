def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        if (i * i) % 2 == 0:
            total += i ** 2
    return total

# Example usage:
n = 10
result = sum_of_squares(n)
print(result)
