def cube_sum(n):
    return n * (n + 1) * (n + 2)

num = int(input("Enter an integer: "))
print(f"The sum of cubes from {num} to {num + 50} is: {cube_sum(num)}")
