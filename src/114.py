def square_root(n):
    if n < 0:
        return None
    else:
        return round((n + 1) ** 0.5)

print(square_root(9))
