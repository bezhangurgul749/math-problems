import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Example equation
equation = x**2 + y**2 - 10

# Solve the equation
solutions = sp.solve(equation, (x, y))

solutions
