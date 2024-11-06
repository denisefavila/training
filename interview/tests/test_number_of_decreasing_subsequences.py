import pytest

from interview.interview.number_of_decreasing_subsequences import \
    get_number_of_decreasing_subsequences


@pytest.mark.parametrize(
    "arr, expected_output",
    [
        ([5, 2, 4, 3, 1, 6], 3),  # Test case 1: Example in description
        (
            [2, 9, 12, 13, 4, 7, 6, 5, 10],
            4,
        ),  # Test case 2: Example with four subsequences
        (
            [1, 1, 1],
            3,
        ),  # Test case 3: All identical elements, each needs its own subsequence
        ([3, 2, 1], 1),  # Test case 4: Already strictly decreasing
        (
            [1, 3, 2, 4, 3, 5],
            4,
        ),  # Test case 5: Alternating increasing and decreasing pattern
        ([10, 8, 6, 4, 2], 1),  # Test case 6: Entirely decreasing
        ([1], 1),  # Test case 7: Single element
        (
            [4, 7, 6, 5, 3],
            2,
        ),  # Test case 8: Partially decreasing with small subsequence
        ([1, 5, 3, 2, 6, 4], 3),  # Test case 9: Complex pattern with mixed order
        (
            [3, 2, 1, 6, 5, 4, 9, 8, 7],
            3,
        ),  # Test case 10: Multiple sections of decreasing subsequences
    ],
)
def test_count_decreasing_subsequences(arr, expected_output):
    assert get_number_of_decreasing_subsequences(arr) == expected_output
