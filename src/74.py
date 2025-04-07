import sympy as sp

def solve_quadratic_equation(a, b, c):
    """
    Solve a quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    - a: Coefficient of x^2
    - b: Coefficient of x
    - c: Constant term
    
    Returns:
    - roots: List containing the solutions (real or complex) to the quadratic equation.
    """
    # Calculate discriminant
    D = b**2 - 4*a*c
    
    if D >= 0:
        # Real roots
        root1 = (-b + sp.sqrt(D)) / (2*a)
        root2 = (-b - sp.sqrt(D)) / (2*a)
        
        return [root1, root2]
    
    elif D == 0:
        # One real root
        x = -b/(2*a)
        return [x]
    
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = sp.sqrt(-D) / (2*a)
        
        return [complex(real_part, imaginary_part), complex(real_part, -imaginary_part)]
