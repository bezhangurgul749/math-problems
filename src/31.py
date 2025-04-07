import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define equations
eq1 = x**2 - 4*x + 3
eq2 = y**2 - 6*y + 9

# Solve the system of equations
solution = sp.solve([eq1, eq2], (x, y))

print(solution)
