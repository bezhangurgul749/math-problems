import math

def find_greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def is_perfect_square(n: int) -> bool:
    sqrt_n = int(math.sqrt(n))
    if sqrt_n * sqrt_n == n:
        return True
    else:
        return False

# Example usage
num1 = 49
num2 = 81

print(f"The greatest common divisor of {num1} and {num2} is: {find_greatest_common_divisor(num1, num2)}")
print(f"Is {num1} a perfect square? {is_perfect_square(num1)}")
print(f"Is {num2} a perfect square? {is_perfect_square(num2)}")
