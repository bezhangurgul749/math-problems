def calculate_expression(expression):
    # Simplify and evaluate the expression using Python's built-in functions
    result = eval(expression)
    return result

expression = "3 + 5 * (2 - 1)"
print(calculate_expression(expression))
