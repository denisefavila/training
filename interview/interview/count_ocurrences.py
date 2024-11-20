def find_first_occurrence(arr, x):
    """
    [1,1,2,2,2,3,4]

    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def find_last_occurrence(arr, x):

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def count_occurrences(arr, x):
    """
    Given a sorted array arr[] and a number x,
    write a function that counts the occurrences of x in arr[].
    [1,1,2,2,2,3,4] -> len(arr) = 7, first_occurrence_idx = 2
    """

    left_idx = find_first_occurrence(arr, x)

    right_idx = find_last_occurrence(arr, x)

    # If x is not found in the array, return 0
    if left_idx <= right_idx:
        return right_idx - left_idx + 1
    else:
        return 0
