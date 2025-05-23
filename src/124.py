import sympy

# Define symbols
x = sympy.Symbol('x')

# Solve the equation
solution = sympy.solve(x**2 - 4*x + 1, x)

# Print the solution
print(solution)
