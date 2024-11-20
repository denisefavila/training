from interview.dp.combination_sum import combination_sum


# Assuming the function to be tested is called "combination_sum"


def test_combination_sum_basic_case():
    C = [2, 3, 6, 7]
    T = 7
    expected = [[2, 2, 3], [7]]
    assert combination_sum(C, T) == expected


def test_combination_sum_no_combinations():
    C = [5, 10, 20]
    T = 3
    expected = []
    assert combination_sum(C, T) == expected


def test_combination_sum_target_is_zero():
    C = [1, 2, 3]
    T = 0
    expected = [[]]
    assert combination_sum(C, T) == expected


def test_combination_sum_single_number_equals_target():
    C = [5]
    T = 5
    expected = [[5]]
    assert combination_sum(C, T) == expected


def test_combination_sum_single_number_not_equals_target():
    C = [5]
    T = 10
    expected = [[5, 5]]
    assert combination_sum(C, T) == expected


def test_combination_sum_all_elements_same():
    C = [2]
    T = 8
    expected = [[2, 2, 2, 2]]
    assert combination_sum(C, T) == expected


def test_combination_sum_no_valid_combinations():
    C = [4, 8, 16]
    T = 3
    expected = []
    assert combination_sum(C, T) == expected


def test_combination_sum_empty_candidates():
    C = []
    T = 10
    expected = []
    assert combination_sum(C, T) == expected


def test_combination_sum_large_input():
    C = [1, 2, 5, 10]
    T = 12
    expected = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 5],
        [1, 1, 1, 1, 1, 1, 2, 2, 2],
        [1, 1, 1, 1, 1, 2, 5],
        [1, 1, 1, 1, 2, 2, 2, 2],
        [1, 1, 1, 2, 2, 5],
        [1, 1, 2, 2, 2, 2, 2],
        [1, 1, 5, 5],
        [1, 1, 10],
        [1, 2, 2, 2, 5],
        [2, 2, 2, 2, 2, 2],
        [2, 5, 5],
        [2, 10],
    ]

    assert combination_sum(C, T) == expected


def test_combination_sum_single_candidate_multiple_target():
    C = [3]
    T = 9
    expected = [[3, 3, 3]]
    assert combination_sum(C, T) == expected
