import sympy as sp

def solve_equation(a, b):
    solution = sp.solve(a * x - b, x)
    return solution

a = 2
b = 4
solution_x = solve_equation(a, b)
print("The solution for the equation is:", solution_x)
