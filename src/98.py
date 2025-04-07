def find_min_value(arr):
    """
    Find the minimum value in an array.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The minimum value in the array.
    """
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

# Example usage and check function
if __name__ == "__main__":
    example_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("The minimum value in the array is:", find_min_value(example_arr))
