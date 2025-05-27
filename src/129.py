import numpy as np

def calculate_sums(data):
    """
    This function takes a list of numerical data and returns a dictionary
    with sums of each pair of elements from the list.
    
    Example usage:
    >>> calculate_sums([10, 20, 30])
    {('sum', (0, 1)): 30, ('sum', (1, 2)): 40, ('sum', (2, 3)): 50}
    """
    sums = {}
    
    for index1 in range(len(data)):
        for index2 in range(index1 + 1, len(data)):
            sum_of_elements = data[index1] + data[index2]
            sums[(tuple([data[index1], data[index2]])), 0:3] = [sum_of_elements]
            if index1 < index2:
                sums[(tuple([data[index1], data[index2]])), 1:4] = [index1, index2]
    return sums

# Example usage
if __name__ == "__main__":
    # Generate some random data for testing purposes
    test_data = np.random.randint(0, 100, size=(3, 3))
    print(calculate_sums(test_data))
