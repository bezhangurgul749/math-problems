def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    else:
        return math.sqrt(num)

try:
    result = square_root(-4)
except ValueError as e:
    print(e) # Output: Cannot compute square root of a negative number
