def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return a * b // gcd(a, b)
