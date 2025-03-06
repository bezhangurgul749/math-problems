import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

num1 = get_random_number(0, 20)
num2 = get_random_number(0, 20)

print("What is", num1, "+", num2, "?")