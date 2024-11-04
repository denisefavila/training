from interview.interview.binary_search.stores_and_houses import get_closest_stores


def test_single_house_and_store():
    # Single house and store at the same location
    assert get_closest_stores([5], [5]) == [5]


def test_single_house_multiple_stores():
    # Single house with multiple stores, one of them is closest
    assert get_closest_stores([10], [5, 15, 8]) == [8]


def test_multiple_houses_single_store():
    # Multiple houses but only one store
    assert get_closest_stores([1, 2, 3, 4], [3]) == [3, 3, 3, 3]


def test_exact_match():
    # Each house has a store at the same location
    assert get_closest_stores([1, 5, 20], [1, 5, 20]) == [1, 5, 20]


def test_equidistant_stores():
    # House has two equidistant stores, return the smallest location
    assert get_closest_stores([7], [5, 9]) == [5]


def test_stores_closer_than_houses():
    # Stores located closer to the houses
    assert get_closest_stores([5, 10, 17], [1, 5, 20, 11, 16]) == [5, 11, 16]


def test_multiple_houses_with_closest_store():
    # Multiple houses with closest store at various distances
    assert get_closest_stores([2, 4, 2], [5, 1, 2, 3]) == [2, 3, 2]


def test_edge_case_identical_locations():
    # Identical house and store locations at the start
    assert get_closest_stores([4, 8, 1, 1], [5, 3, 1, 2, 6]) == [3, 6, 1, 1]


def test_no_houses():
    # Edge case with no houses
    assert get_closest_stores([], [5, 10, 15]) == []


def test_no_stores():
    # Edge case with no stores
    assert get_closest_stores([1, 2, 3], []) == []
