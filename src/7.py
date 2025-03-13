import random

def get_random_code():
    # Generate a random number between 1 and 100
    num = random.randint(1, 100)

    # Use the random number to generate a random code
    code = ''.join([str(num % i) for i in range(2, 10)])

    return code
