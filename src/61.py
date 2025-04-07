import sympy as sp
from sympy import symbols

x = symbols('x')
f = x**2 - 5*x + 6

for i in range(10):
    f = f.subs(x, i)
    
print(f)
