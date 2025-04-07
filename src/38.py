def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def calculate_square_root(x: float) -> float:
    """Calculate the square root of a number."""
    return x ** 0.5

def display_menu():
    print("Choose an operation:")
    print("1. Add two numbers")
    print("2. Calculate the square root")
    print("3. Exit")

if __name__ == "__main__":
    # Main program
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        a, b = map(int, input("Enter two numbers to add: ").split())
        result = add_numbers(a, b)
        print(f"The sum of {a} and {b} is: {result}")
    elif choice == '2':
        x = float(input("Enter a number: "))
        square_root = calculate_square_root(x)
        print(f"The square root of {x} is: {square_root}")
    elif choice == '3':
        print("Exiting the program.")
    else:
        print("Invalid input. Please enter 1, 2 or 3.")

    # Display menu after main
