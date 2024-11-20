from interview.interview.and_or_function import get_or, get_and


# Assuming get_or and get_and functions are implemented as described


def test_union_intervals():
    V1 = [(2, 4), (6, 8), (1, 3)]
    V2 = [(7, 9), (2, 5)]
    expected_union = [(1, 5), (6, 9)]
    assert get_or(V1, V2) == expected_union


def test_union_no_overlap():
    V1 = [(1, 2), (3, 4)]
    V2 = [(5, 6), (7, 8)]

    expected_union = [(1, 2), (3, 4), (5, 6), (7, 8)]
    assert get_or(V1, V2) == expected_union


def test_union_full_overlap():
    V1 = [(1, 5)]
    V2 = [(2, 4)]
    expected_union = [(1, 5)]
    assert get_or(V1, V2) == expected_union


def test_union_empty_v2():
    V1 = [(1, 2), (3, 5)]
    V2 = []
    expected_union = [(1, 2), (3, 5)]
    assert get_or(V1, V2) == expected_union


def test_get_and():
    # Test Case 1: Basic intersection
    intervals1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
    intervals2 = [[1, 5], [8, 12], [15, 24], [25, 26]]
    expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert get_and(intervals1, intervals2) == expected

    # Test Case 2: No intersection
    intervals1 = [(1, 2), (3, 4)]
    intervals2 = [(5, 6), (7, 8)]
    expected = []
    assert get_and(intervals1, intervals2) == expected

    # Test Case 3: Full overlap
    intervals1 = [(1, 5), (8, 12)]
    intervals2 = [(2, 6), (7, 10)]
    expected = [[2, 5], [8, 10]]
    assert get_and(intervals1, intervals2) == expected

    # Test Case 4: Partial overlap
    intervals1 = [(1, 5), (8, 12)]
    intervals2 = [(3, 6), (7, 10)]
    expected = [[3, 5], [8, 10]]
    assert get_and(intervals1, intervals2) == expected

    # Test Case 5: Overlapping intervals with no intersection
    intervals1 = [(1, 2), (5, 6)]
    intervals2 = [(3, 4), (7, 8)]
    expected = []
    assert get_and(intervals1, intervals2) == expected

    # Test Case 6: Intervals with exact same range
    intervals1 = [(1, 3), (4, 6)]
    intervals2 = [(1, 3), (4, 6)]
    expected = [[1, 3], [4, 6]]
    assert get_and(intervals1, intervals2) == expected

    # Test Case 7: One list is empty
    intervals1 = []
    intervals2 = [(2, 5), (7, 9)]
    expected = []
    assert get_and(intervals1, intervals2) == expected

    # Test Case 8: Intersection at the boundary
    intervals1 = [(1, 4), (6, 8)]
    intervals2 = [(4, 5), (7, 9)]
    expected = [[4, 4], [7, 8]]
    assert get_and(intervals1, intervals2) == expected

    # Test Case 9: Overlapping intervals with exact matching
    intervals1 = [(1, 5)]
    intervals2 = [(1, 5)]
    expected = [[1, 5]]
    assert get_and(intervals1, intervals2) == expected

    # Test Case 10: No intersection, second starts after first ends
    intervals1 = [(1, 2), (3, 4)]
    intervals2 = [(5, 6)]
    expected = []
    assert get_and(intervals1, intervals2) == expected
