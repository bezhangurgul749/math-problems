def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

print(fibonacci(10))
