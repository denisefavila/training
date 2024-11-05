from interview.interview.longest_increasing_subsequence import longest_increasing_subsequence

import pytest


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),  # Empty list
        ([10], 1),  # Single element
        ([1, 2, 3, 4, 5], 5),  # Strictly increasing list
        ([5, 4, 3, 2, 1], 1),  # Strictly decreasing list
        ([2, 2, 2, 2, 2], 1),  # All elements the same
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # Mixed elements
        ([1, 3, 3, 3, 4, 5], 4),  # Consecutive duplicates with increasing subsequence
        ([1, 3, 2, 4, 3, 5], 4),  # Alternating increase and decrease
        (
            [1, 2, 0, 3, 0, 4, 0, 5],
            5,
        ),  # Large increasing with small interspersed values
    ],
)
def test_longest_increasing_subsequence(nums, expected):
    assert longest_increasing_subsequence(nums) == expected
