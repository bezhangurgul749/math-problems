import random

def get_random_math_problem():
    """Returns a random math problem in the format (operation, operands)."""
    operation = random.choice(["+", "-", "*", "/"])
    operands = [random.randint(1, 10), random.randint(1, 10)]
    return (operation, operands)

def solve_math_problem(problem):
    """Solves a math problem in the format (operation, operands)."""
    operation = problem[0]
    operands = problem[1]
    if operation == "+":
        return operands[0] + operands[1]
    elif operation == "-":
        return operands[0] - operands[1]
    elif operation == "*":
        return operands[0] * operands[1]
    else:
        return operands[0] / operands[1]
