from interview.interview.count_ocurrences import count_occurrences


# Test cases for the count_occurrences function
def test_count_occurrences():
    # Test case 1: Simple case where x is present multiple times
    assert count_occurrences([1, 2, 2, 2, 3, 4, 5], 2) == 3

    # Test case 2: x is present once
    assert count_occurrences([1, 2, 3, 4, 5], 3) == 1

    # Test case 3: x is not present in the array
    assert count_occurrences([1, 2, 3, 4, 5], 6) == 0

    # Test case 4: x is at the start of the array
    assert count_occurrences([1, 1, 2, 3, 4, 5], 1) == 2

    # Test case 5: x is at the end of the array
    assert count_occurrences([1, 2, 3, 4, 4, 4], 4) == 3

    # Test case 6: Empty array
    assert count_occurrences([], 5) == 0

    # Test case 7: Large input where x occurs many times
    arr = [1] * 1000000  # Array of 1 million 1's
    assert count_occurrences(arr, 1) == 1000000

    # Test case 8: Array with all elements being the same, and x is that element
    assert count_occurrences([3, 3, 3, 3, 3], 3) == 5

    # Test case 9: Array with one element, and x is that element
    assert count_occurrences([42], 42) == 1

    # Test case 10: Array with one element, but x is not that element
    assert count_occurrences([42], 50) == 0
