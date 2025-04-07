import sympy as sp

def solve_polynomial(coeffs):
    x = sp.symbols('x')
    result = sp.solve(coeffs[0]*x**2 + coeffs[1]*x + coeffs[2], x)
    return result

# Example usage:
coeffs = [1, -3, 2]  # Coefficients for the polynomial: 1*x^2 - 3*x + 2
print(solve_polynomial(coeffs))
