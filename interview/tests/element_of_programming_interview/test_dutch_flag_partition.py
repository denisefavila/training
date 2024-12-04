from interview.interview.elements_of_programming_interview.dutch_flag_partition import (
    dutch_flag_partition,
)


def test_dutch_flag_partition():

    arr = [0, 1, 2, 0, 2, 3, 1, 1, 3]
    dutch_flag_partition(2, arr)  # pivot_idx = 3, arr[3] = 0
    assert arr == [0, 1, 0, 1, 1, 2, 2, 3, 3]  # Expected output

    # Test 1: General case
    arr = [0, 1, 2, 0, 2, 1, 1]
    dutch_flag_partition(3, arr)  # pivot_idx = 3, arr[3] = 0
    assert arr == [0, 0, 1, 2, 2, 1, 1]  # Expected output

    # Test 2: All elements equal to the pivot
    arr = [1, 1, 1, 1]
    dutch_flag_partition(0, arr)  # pivot_idx = 0, arr[0] = 1
    assert arr == [1, 1, 1, 1]  # No change expected as all are the same

    # Test 3: All elements smaller than the pivot
    arr = [0, 0, 0, 0]
    dutch_flag_partition(0, arr)  # pivot_idx = 0, arr[0] = 0
    assert arr == [0, 0, 0, 0]  # No change expected as all are the same

    # Test 4: All elements larger than the pivot
    arr = [2, 2, 2, 2]
    dutch_flag_partition(0, arr)  # pivot_idx = 0, arr[0] = 2
    assert arr == [2, 2, 2, 2]  # No change expected as all are the same
