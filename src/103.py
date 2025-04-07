import sympy as sp

def solve_linear_equation(a, b, c):
    """
    Solve a linear equation of the form: ax + b = c.
    
    Parameters:
    a (int): Coefficient of x in the equation.
    b (int): Constant term in the equation.
    c (int): Constant value on one side of the equation.
    
    Returns:
    tuple: A list containing the solutions for the linear equation, or None if no solution exists.
    """
    try:
        # Solve the linear equation
        x = sp.solve(a*sp.Symbol('x') + b - c, sp.Symbol('x'))
        
        return x
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
solution = solve_linear_equation(1, 2, 5)
print(f"The solutions are: {solution}")
