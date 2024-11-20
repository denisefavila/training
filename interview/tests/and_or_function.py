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


def test_intersection_intervals():
    V1 = [(2, 4), (6, 8), (1, 3)]
    V2 = [(7, 9), (2, 5)]
    expected_intersection = [(2, 4)]
    assert get_and(V1, V2) == expected_intersection


def test_intersection_no_overlap():
    V1 = [(1, 2), (3, 4)]
    V2 = [(5, 6), (7, 8)]
    expected_intersection = []
    assert get_and(V1, V2) == expected_intersection


def test_intersection_full_overlap():
    V1 = [(1, 5)]
    V2 = [(1, 5)]
    expected_intersection = [(1, 5)]
    assert get_and(V1, V2) == expected_intersection


def test_intersection_partial_overlap():
    V1 = [(1, 5)]
    V2 = [(3, 7)]
    expected_intersection = [(3, 5)]
    assert get_and(V1, V2) == expected_intersection


def test_intersection_empty_v2():
    V1 = [(1, 2), (3, 5)]
    V2 = []
    expected_intersection = []
    assert get_and(V1, V2) == expected_intersection


def test_intersection_with_disjoint_intervals():
    V1 = [(1, 2), (5, 6)]
    V2 = [(3, 4), (7, 8)]
    expected_intersection = []
    assert get_and(V1, V2) == expected_intersection
