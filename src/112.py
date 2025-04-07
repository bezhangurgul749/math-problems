import sympy as sp

def solve_equation(a, b):
    x = sp.symbols('x')
    equation = sp.Eq(x ** 3 + a * x - b, 0)
    solutions = sp.solve(equation, x)
    return solutions

# Example usage:
a = 1
b = 2
print(solve_equation(a, b))
