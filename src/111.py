import math
from sympy import symbols, solve

x = symbols('x')
equation = 2*x**3 - 5*x**2 + 7*x - 10

roots = solve(equation)
roots
