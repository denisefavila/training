import pytest
from typing import List, Tuple

from interview.interview.smallest_subarray_with_k_distinct_elements import (
    smallest_subarray_with_k_distinct,
)


@pytest.mark.parametrize(
    "A, K, expected",
    [
        # Simple cases
        (
            [1, 2, 2, 3, 1, 3],
            2,
            (0, 1),
        ),  # Subarray [1, 2] is the smallest with 2 distinct integers
        (
            [1, 2, 1, 3, 4],
            3,
            (1, 4),
        ),  # Subarray [2, 1, 3, 4] is the smallest with 3 distinct integers
        ([1, 2, 3, 4, 5], 5, (0, 4)),  # The entire array is needed
        ([1, 1, 1, 1], 1, (0, 0)),  # Single element subarray [1]
        # Edge cases
        ([1, 2], 3, None),  # Not enough distinct elements
        ([1, 2, 3], 0, None),  # Invalid K
        # Complex cases
        ([1, 2, 1, 3, 2, 4], 3, (1, 4)),  # Subarray [2, 1, 3, 4] is the smallest
        ([1, 1, 2, 2, 3, 3], 2, (0, 1)),  # Prioritize the leftmost subarray [1, 2]
        ([5, 5, 1, 1, 3, 3], 2, (0, 1)),  # Repeated numbers, subarray [5, 1]
        (
            [1, 2, 1, 3, 4, 2, 1],
            3,
            (1, 4),
        ),  # Subarray [2, 1, 3, 4] with smallest leftmost index
    ],
)
def test_smallest_subarray_with_k_distinct(
    A: List[int], K: int, expected: Tuple[int, int]
):
    """
    Test smallest_subarray_with_k_distinct with various inputs and expected outputs.
    """
    result = smallest_subarray_with_k_distinct(A, K)
    assert (
        result == expected
    ), f"For A={A} and K={K}, expected {expected} but got {result}"
