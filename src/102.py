def calculate_sum(a: int, b: int) -> int:
    return a + b

def find_max_integer(lst: list) -> int:
    max_int = lst[0]
    for num in lst:
        if num > max_int:
            max_int = num
    return max_int
