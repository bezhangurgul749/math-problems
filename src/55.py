import sympy

# Define symbols
x = sympy.Symbol('x')
equation = x**2 - 4*x + 1

# Solve the equation
solutions = sympy.solve(equation, x)
print(solutions)
