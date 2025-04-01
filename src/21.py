import sympy
from sympy import *
x, y = symbols('x y')

# Define symbolic expressions
expr1 = x + 2*y - 5
expr2 = (x - y)*(x - 4) - (x + 3)

# Simplify the expressions and compare
simplified_expr1 = simplify(expr1)
simplified_expr2 = simplify(expr2)

print(simplified_expr1)
print(simplified_expr2)
