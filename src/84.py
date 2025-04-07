# Example of generating random code within certain constraints
import random

def random_code_generator(code_length=10):
    """
    Generate a random code with a specified length.
    Constraints: The generated code should be between 4 and 6 characters in length.

    :param code_length: Length of the code to generate (default is 10)
    :type code_length: int
    :return: A random code within the given constraints
    :rtype: str
    """
    if not isinstance(code_length, int) or code_length < 4 or code_length > 6:
        raise ValueError("Code length must be between 4 and 6 characters.")

    # Ensure code_length is an even number to maintain a consistent pattern
    code_length = code_length % 2 + 1

    # Generate the random code
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=code_length))

# Example usage and output
random_code = random_code_generator()
print(f"Generated Random Code: {random_code}")
