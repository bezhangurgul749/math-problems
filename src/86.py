import sympy as sp

# Define symbols for the problem
x, y = sp.symbols('x y')

# Equation 1: x^2 + y^2 = 1
equation1 = x**2 + y**2 - 1

# Solve equation 1 to find solutions (x, y)
solutions = sp.solve(equation1, (x, y))
print(solutions)
