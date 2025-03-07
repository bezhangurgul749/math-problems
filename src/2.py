import random

def get_random_code(length):
    # Generate a random string of letters and digits
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    characters = letters + numbers
    code = ''.join(random.choice(characters) for i in range(length))
    return code