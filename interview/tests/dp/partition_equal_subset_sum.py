from interview.dp.partition_equal_subset_sum import can_partition


def test_partition_possible():
    # Test Case 2: The array cannot be partitioned into two subsets with equal sum
    nums = [1, 2, 3, 5]
    assert not can_partition(nums)

    # Test Case 1: The array can be partitioned into two subsets with equal sum
    nums = [1, 5, 11, 5]
    assert can_partition(nums)

    # Test Case 3: The array can be partitioned into two subsets with equal sum (edge case)
    nums = [10, 10]
    assert can_partition(nums)

    # Test Case 4: The array is already balanced (each number is 0)
    nums = [0, 0, 0, 0]
    assert can_partition(nums)

    # Test Case 5: The array has a single element (odd case)
    nums = [1]
    assert not can_partition(nums)

    # Test Case 6: Empty array, should return True as the sum is zero
    nums = []
    assert can_partition(nums)

    # Test Case 7: All elements are the same
    nums = [2, 2, 2, 2]
    assert can_partition(nums)

    # Test Case 8
    nums = [1, 2, 3]
    assert can_partition(nums)

    # Test Case 9: Large test case where partitioning is possible
    nums = [1] * 1000 + [2] * 1000
    assert can_partition(nums)

    # Test Case 10: Large test case where partitioning is impossible
    nums = [1] * 1000 + [3] * 1000
    assert can_partition(nums)
