import sympy as sp

x = sp.symbols('x')
eq1 = x**2 - 5*x + 6
simplified_eq = sp.simplify(eq1)
print(simplified_eq)
