def is_divisible(n, m):
    return n % m == 0

def find_factors_sum(num):
    sum = 1
    for i in range(2, num // 2 + 1):
        if (num - i) / i > 0:
            sum += i
    return sum

def main():
    print("Enter a number: ", end="")
    n = int(input())

    if is_divisible(n, 4):
        print(f"{n} is divisible by {4}.")
    else:
        print(f"{n} is not divisible by 4.")

    print("Enter another number (or use 0 to exit): ", end="")
    num_to_check = int(input()) if input() != "0" else 0

    sum_of_factors = find_factors_sum(num_to_check)
    print(f"The sum of the factors of {num_to_check} is: {sum_of_factors}")

if __name__ == "__main__":
    main()
