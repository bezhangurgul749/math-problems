import sympy

def solve_polynomial(coefficients):
    """
    Solve a polynomial equation ax^n + bx^(n-1) + ... + z = 0.
    
    Parameters:
        coefficients (list): A list of coefficients [a, b, c, ..., z].
        
    Returns:
        result (float or int): The solution of the equation.
    """
    # Get the coefficient matrix and the constant term
    coo_matrix = sympy.Matrix(coefficients).transpose()
    
    # Solve for x using sympy's solve function with the matrix being upper triangular
    result = coo_matrix.solve(sympy.Matrix([[1], [0, 1]]))
    
    return result[0]

# Example usage and check (not a complete solution)
if __name__ == "__main__":
    # Coefficients for a polynomial equation ax^n + bx^(n-1) + c = 0
    x_coefficients = [2, -3, 4]
    y_coefficients = [-1, 5, -6]
    
    print("Polynomial coefficients:", x_coefficients, y_coefficients)
    solution = solve_polynomial(x_coefficients + y_coefficients)
    print("Solution of the equation ax^n + bx^(n-1) + c = 0 is:", solution)
