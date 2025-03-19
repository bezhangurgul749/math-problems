from random import randint

def solve_math_problem(problem):
    """
    Solves a math problem in the form of an equation.

    Args:
        problem (str): The math problem to be solved.

    Returns:
        The solution to the math problem.
    """
    numbers = []
    operators = ["+", "-", "*", "/"]

    for char in problem:
        if char.isdigit():
            numbers.append(int(char))
        elif char in operators:
            return eval("".join(numbers) + char + "".join(numbers[1:]))

    return None