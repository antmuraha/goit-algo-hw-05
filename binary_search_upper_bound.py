def binary_search_upper_bound(sorted_array: list[int | float], target: int | float) -> tuple[int, int | float]:
    """
    sorted_array: Sorted list of numbers (int or float).
    target: Search value.
    return: Tuple (number of iterations, upper bound).
    """
    left, right = 0, len(sorted_array) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if sorted_array[mid] == target:
            return iterations, sorted_array[mid]
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            upper_bound = sorted_array[mid]
            right = mid - 1

    # If we don't find the exact element, we return the nearest upper bound
    if upper_bound is None and left < len(sorted_array):
        upper_bound = sorted_array[left]

    return iterations, upper_bound


if __name__ == "__main__":
    # Testing
    sorted_array = [0.7, 1.3, 3.5, 4.7, 7.9, 10.1]
    print("List:", sorted_array)

    for target in [-10, 0, 1, 2, 7, 10, 100]:
        result = binary_search_upper_bound(sorted_array, target)
        print("\nTarget:", target)
        print("Number of iterations:", result[0])
        print("Upper bound:", result[1])
