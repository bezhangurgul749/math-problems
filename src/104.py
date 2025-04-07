import sympy as sp
from sympy import symbols, Eq, solve

x = symbols('x')
f = x**2 - 5*x + 6
solutions = solve(f, x)
print(solutions)
