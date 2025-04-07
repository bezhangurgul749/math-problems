import sympy

# Define symbols
x, y = sympy.symbols('x y')

# Solve the system of equations
solution = sympy.solve((x**2 - 4*x*y + y**2 - 10, x - 2*y), (x, y))

# Print the solution
print(solution)
