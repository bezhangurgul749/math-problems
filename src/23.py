import random
def generate_random_number(min_value: int, max_value: int) -> int:
    """
    Generate a random number between min_value and max_value (inclusive).

    :param min_value: The minimum value of the range.
    :param max_value: The maximum value of the range.
    :return: A randomly generated integer within the given range.
    """
    return random.randint(min_value, max_value)
