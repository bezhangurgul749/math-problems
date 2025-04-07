def calculate_sum(a, b):
    return a + b

def main():
    print("Enter two numbers:")
    num1 = float(input())
    num2 = float(input())
    result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
