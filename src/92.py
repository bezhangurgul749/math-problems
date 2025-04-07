def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not defined")
    sqrt_val = x ** 0.5
    return sqrt_val

try:
    print(square_root(-4))
except ValueError as e:
    print(e)
