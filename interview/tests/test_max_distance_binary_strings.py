from interview.interview.max_distance_binary_strings import (
    get_max_distance_binary_strings,
)


def test_max_distance():
    # Test case 1: Basic test case
    binary_strings = ["1011000", "1011110"]
    assert get_max_distance_binary_strings(binary_strings) == 6

    # Test case 2: No common prefix
    binary_strings = ["1100", "0011"]
    assert get_max_distance_binary_strings(binary_strings) == 8  # Lengths: 4 + 4

    # Test case 3: All strings are identical
    binary_strings = ["101010", "101010", "101010"]
    assert (
        get_max_distance_binary_strings(binary_strings) == 0
    )  # No distance if all are identical

    # Test case 4: Strings of different lengths
    binary_strings = ["111", "1100", "1001"]
    assert (
        get_max_distance_binary_strings(binary_strings) == 6
    )  # max distance between "111" and "1001" or "1100"

    # Test case 5: Longer strings with common prefixes
    binary_strings = ["1101001", "1101010", "1101111"]
    assert (
        get_max_distance_binary_strings(binary_strings) == 6
    )  # Distance between "1101001" and "1101111"

    # Test case 6: Empty input list
    binary_strings = []
    assert (
        get_max_distance_binary_strings(binary_strings) == 0
    )  # No strings, so distance is 0

    # Test case 7: Single string in the list
    binary_strings = ["1100"]
    assert (
        get_max_distance_binary_strings(binary_strings) == 0
    )  # Only one string, distance is 0

    binary_strings = ["1000", "1111", "111100000000", "111111111111"]
    assert get_max_distance_binary_strings(binary_strings) == 16
